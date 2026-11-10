#!/usr/bin/env python3
"""Read-only structural/content audit; no rendering, visual or mathematical review."""
import argparse
import base64
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

try:
    import fitz
    from bs4 import BeautifulSoup, NavigableString, Tag
except ImportError as exc:
    sys.exit(f"Missing dependency: {exc}. Use an existing Python with bs4 and PyMuPDF; no automatic installation.")

FORMULA_SELECTOR = '.katex, mjx-container, .MathJax, .MathJax_SVG, math'
TEX_RE = re.compile(r'\\(?:frac|dfrac|tfrac|sqrt|begin|end|boxed|tag|text|displaystyle|left|right)\b|(?:d?frac|sqrt)\s*\{|\$\$|\\[\[\]]')
CSS_REF_RE = re.compile(r'url\(\s*[\'\"]?([^\)\'\"]+)[\'\"]?\s*\)|@import\s+[\'\"]([^\'\"]+)[\'\"]', re.I)
FONT_FACE_RE = re.compile(r'@font-face\s*\{([^{}]*)\}', re.I | re.S)
FONT_SRC_RE = re.compile(r'(?:^|;)\s*src\s*:\s*(.*?)(?=;|$)', re.I | re.S)
FONT_URL_RE = re.compile(r'url\(\s*(?P<q>[\'\"]?)(?P<url>[^\)\'\"]+)(?P=q)\s*\)\s*(?:format\([^)]*\))?', re.I)


def norm(value):
    return re.sub(r'\s+', '', value)


def digest(value):
    return hashlib.sha256(value).hexdigest()


def canonical(node):
    if isinstance(node, NavigableString):
        return norm(str(node))
    if not isinstance(node, Tag):
        return ''
    attrs = {}
    for key, val in sorted(node.attrs.items()):
        attrs[key] = sorted(val) if isinstance(val, list) else val
    children = [canonical(child) for child in node.children]
    return [node.name, attrs, [child for child in children if child != '']]


def formula_nodes(root):
    candidates = root.select(FORMULA_SELECTOR)
    ids = {id(node) for node in candidates}
    return [node for node in candidates if not any(id(p) in ids for p in node.parents)]


def load_html(path, selector):
    soup = BeautifulSoup(path.read_text(encoding='utf-8'), 'html.parser')
    roots = soup.select(selector)
    if len(roots) != 1:
        raise ValueError(f'content selector must match exactly one node: {selector!r}, got {len(roots)}')
    root = roots[0]
    # Work on a detached parse, never alter the supplied source or caller's DOM.
    clean = BeautifulSoup(str(root), 'html.parser')
    for node in clean.select('script, style'):
        node.decompose()
    formulas = formula_nodes(clean)
    formula_records = []
    for node in formulas:
        annotations = [n.get_text() for n in node.select('annotation')]
        formula_records.append({
            'engine_node': node.name,
            'source': annotations or ([node.get('data-tex')] if node.has_attr('data-tex') else []),
            'dom_sha256': digest(json.dumps(canonical(node), ensure_ascii=False, sort_keys=True).encode()),
        })
    text = norm(clean.get_text())
    # Formula annotations legitimately contain TeX; inspect only surrounding prose.
    plain = BeautifulSoup(str(clean), 'html.parser')
    for node in formula_nodes(plain):
        node.decompose()
    unrendered = []
    for node in clean.select('.math'):
        rendered_self = node.name in ('math', 'mjx-container') or any(
            c in node.get('class', []) for c in ('katex', 'MathJax', 'MathJax_SVG'))
        if not rendered_self and not node.select_one(FORMULA_SELECTOR):
            unrendered.append(node.get_text()[:160])
    return {
        'soup': soup, 'root': root, 'text': text, 'formulas': formula_records,
        'errors': [str(n)[:240] for n in soup.select('.katex-error, .katex-render-error, mjx-merror, .MathJax_Error, .MathJax_SVG_Error, merror')],
        'unrendered_math': unrendered,
        'tex_in_prose': [m.group(0) for m in TEX_RE.finditer(plain.get_text())],
    }


def read_resource(url, base):
    absolute = urljoin(base, url.strip())
    parsed = urlsplit(absolute)
    if parsed.scheme in ('http', 'https'):
        return absolute, 'remote', None
    if parsed.scheme == 'data':
        header, body = absolute.split(',', 1)
        data = base64.b64decode(body) if ';base64' in header else unquote(body).encode()
        return absolute[:80] + '...', 'embedded', data
    if parsed.scheme != 'file' or parsed.netloc not in ('', 'localhost'):
        return absolute, 'unsupported_scheme', None
    path = Path(unquote(parsed.path))
    if not path.is_file():
        return str(path), 'missing', None
    return str(path), 'local', path.read_bytes()


def resource_audit(path, soup):
    refs = []
    seen_css = set()
    base = path.as_uri()
    base_tag = soup.find('base', href=True)
    if base_tag:
        base = urljoin(base, base_tag['href'])

    def inspect(url, origin, source_base):
        if not url or url.startswith('#'):
            return None
        try:
            location, status, data = read_resource(url, source_base)
            record = {'url': url[:400], 'origin': origin, 'resolved': location,
                      'status': status}
            refs.append(record)
            if data is not None and urlsplit(location).path.lower().endswith('.css') and location not in seen_css:
                seen_css.add(location)
                css_base = Path(location).as_uri() if status == 'local' else source_base
                scan_css(data.decode('utf-8', errors='replace'), location, css_base)
            return record
        except (OSError, ValueError) as exc:
            refs.append({'url': url[:400], 'origin': origin, 'status': 'unreadable', 'error': str(exc)})
            return refs[-1]

    def font_fallback_groups(css):
        """Recognize only simple comma-separated @font-face url() alternatives."""
        groups = []
        for block in FONT_FACE_RE.finditer(css):
            sources = list(FONT_SRC_RE.finditer(block.group(1)))
            if len(sources) != 1:
                continue
            source = sources[0]
            value = source.group(1)
            # Keep var(), local(), data URIs and other complex CSS on the strict path.
            if re.search(r'\b(?:var|local)\s*\(|data:', value, re.I):
                continue
            urls = list(FONT_URL_RE.finditer(value))
            if len(urls) < 2 or any(not m.group('url').strip() for m in urls):
                continue
            if value[:urls[0].start()].strip() or value[urls[-1].end():].strip():
                continue
            if any(value[left.end():right.start()].strip() != ',' for left, right in zip(urls, urls[1:])):
                continue
            groups.append((block.start(1) + source.start(1),
                           block.start(1) + source.end(1),
                           [m.group('url').strip() for m in urls]))
        return groups

    def scan_css(css, origin, source_base):
        groups = font_fallback_groups(css)
        # Inspect each simple @font-face source set as a unit. Missing alternatives
        # are warnings only when another candidate is locally/embedded available.
        for _, _, group in groups:
            candidates = [inspect(url, f'{origin} @font-face src candidate', source_base) for url in group]
            usable = any(candidate and candidate.get('status') in ('local', 'embedded') for candidate in candidates)
            if usable:
                for candidate in candidates:
                    if candidate and candidate.get('status') == 'missing':
                        candidate['status'] = 'missing_fallback'
                        candidate['warning'] = 'Fallback candidate missing; another local/embedded font source exists, but actual selection was not verified'
        for match in CSS_REF_RE.finditer(css):
            url = (match.group(1) or match.group(2)).strip()
            # Avoid checking recognized @font-face candidates twice as ordinary URLs.
            if any(start <= match.start() < end for start, end, _ in groups):
                continue
            inspect(url, origin, source_base)

    for tag in soup.find_all(True):
        for attr in ('src', 'poster', 'data' if tag.name == 'object' else '___'):
            if tag.get(attr):
                inspect(tag[attr], f'{tag.name}[{attr}]', base)
        if tag.name == 'link' and tag.get('href'):
            rel = set(tag.get('rel', []))
            if rel & {'stylesheet', 'icon', 'preload', 'modulepreload', 'prefetch', 'manifest'}:
                inspect(tag['href'], 'link[href]', base)
        if tag.get('srcset'):
            # Embedded srcset syntax needs a browser parser; do not silently certify it.
            if 'data:' in tag['srcset']:
                refs.append({'status': 'unsupported_srcset', 'origin': f'{tag.name}[srcset]'})
            else:
                for item in tag['srcset'].split(','):
                    if item.strip():
                        inspect(item.strip().split()[0], f'{tag.name}[srcset]', base)
        css = tag.get('style', '') + (tag.get_text() if tag.name == 'style' else '')
        if css:
            scan_css(css, 'inline CSS', base)
    warnings = [r for r in refs if r['status'] == 'missing_fallback']
    return {
        'status': 'failed' if any(r['status'] not in ('local', 'embedded', 'missing_fallback') for r in refs) else 'passed',
        'scope': 'Static HTML references plus recursive CSS url()/@import regex; simple @font-face src URL alternatives are grouped, but no browser execution',
        'warnings': warnings,
        'limitations': ['Static resource checks do not prove actual font selection/rendering and do not detect JavaScript-created requests, CSS syntax beyond simple url/import patterns, or PDF external actions. Not a complete offline runtime certification.'],
        'resources': refs,
    }, base


def images(root, base):
    records = []
    for node in root.select('img'):
        src = node.get('src', '')
        try:
            location, status, data = read_resource(src, base) if src else ('', 'missing_src', None)
            records.append({'alt': node.get('alt', ''), 'sha256': digest(data) if data is not None else None,
                            'status': status, 'resolved': location})
        except (ValueError, OSError) as exc:
            records.append({'alt': node.get('alt', ''), 'sha256': None, 'status': 'unreadable', 'error': str(exc)})
    return records


def compare_lists(left, right):
    first = next((i for i, pair in enumerate(zip(left, right)) if pair[0] != pair[1]), None)
    return {'status': 'passed' if left == right else 'failed', 'baseline_count': len(left),
            'variant_count': len(right), 'first_mismatch_index_0based': first if first is not None else (min(len(left), len(right)) if len(left) != len(right) else None)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--html', required=True, type=Path)
    parser.add_argument('--pdf', required=True, type=Path)
    parser.add_argument('--baseline', type=Path, help='Already-rendered reference HTML; no source modifications')
    parser.add_argument('--content-selector', default='body', help='Exactly one matching node in both HTML files')
    parser.add_argument('--expect-pages', type=int)
    parser.add_argument('--require-outline', action='store_true')
    parser.add_argument('--expected-outline', type=Path, help='JSON object {"Title": 1} or list of {"title": "Title", "page": 1}; one-based PDF pages')
    parser.add_argument('--author', default='chengbai', help='Exact expected PDF author metadata')
    parser.add_argument('--report', required=True, type=Path)
    parser.add_argument('--preview-dir', type=Path, help='New or empty directory; creates 72dpi page PNGs and contact.jpg')
    parser.add_argument('--replace', action='store_true', help='Allow replacing an existing report; previews still require an empty directory')
    args = parser.parse_args()
    if args.expect_pages is not None and args.expect_pages < 1:
        parser.error('--expect-pages must be positive')
    protected = [p.resolve() for p in (args.html, args.pdf, args.baseline, args.expected_outline) if p]
    if args.report.resolve() in protected:
        parser.error('report cannot overwrite an input, even with --replace')
    if args.report.exists() and not args.replace:
        parser.error('report already exists; choose a new path or pass --replace')
    if args.preview_dir and args.preview_dir.exists() and (not args.preview_dir.is_dir() or any(args.preview_dir.iterdir())):
        parser.error('preview directory must be new or empty; existing previews are never overwritten')
    report = {'schema_version': 1, 'created_utc': datetime.now(timezone.utc).isoformat(),
              'inputs': {'html': str(args.html.resolve()), 'pdf': str(args.pdf.resolve()),
                         'baseline': str(args.baseline.resolve()) if args.baseline else None},
              'visual_review': 'not_performed', 'mathematical_review': 'not_performed',
              'pdf_body_content_fidelity': 'not_checked',
              'limitations': ['HTML-to-HTML fidelity does not prove all content is visible or present in the PDF.', 'Machine checks do not establish visual correctness, mathematical correctness, or correct navigation targets.'],
              'checks': {}, 'content_fidelity': {'status': 'not_checked', 'reason': 'No baseline supplied'},
              'previews': {'status': 'not_requested'}}
    checks = report['checks']
    html = None
    try:
        html = load_html(args.html.resolve(), args.content_selector)
        checks['html_rendering'] = {'status': 'failed' if html['errors'] or html['unrendered_math'] or html['tex_in_prose'] else 'passed',
                                    'render_errors': html['errors'], 'unrendered_math': html['unrendered_math'],
                                    'tex_in_prose': html['tex_in_prose'], 'formula_count': len(html['formulas'])}
        checks['offline_static_resources'], base = resource_audit(args.html.resolve(), html['soup'])
        current_images = images(html['root'], base)
        checks['html_images'] = {'status': 'failed' if any(i['sha256'] is None for i in current_images) else 'passed', 'items': current_images}
        if args.baseline:
            old = load_html(args.baseline.resolve(), args.content_selector)
            _, old_base = resource_audit(args.baseline.resolve(), old['soup'])
            old_images = images(old['root'], old_base)
            text_comparison = compare_lists(list(old['text']), list(html['text']))
            formula_comparison = compare_lists(old['formulas'], html['formulas'])
            image_comparison = compare_lists([(i['sha256'], i['alt']) for i in old_images], [(i['sha256'], i['alt']) for i in current_images])
            if any(i['sha256'] is None for i in old_images + current_images):
                image_comparison['status'] = 'failed'
                image_comparison['reason'] = 'Unreadable image bytes cannot establish fidelity'
            baseline_ok = not old['errors'] and not old['unrendered_math'] and not old['tex_in_prose']
            passed = baseline_ok and all(c['status'] == 'passed' for c in (text_comparison, formula_comparison, image_comparison))
            report['content_fidelity'] = {'status': 'passed' if passed else 'failed',
                'scope': 'Selected HTML content only; whitespace-insensitive text order, exact canonical rendered formula DOM, image byte hashes and alt order',
                'baseline_rendered': baseline_ok, 'body_text': text_comparison,
                'formulas': formula_comparison, 'images': image_comparison,
                'baseline_text_sha256': digest(old['text'].encode()), 'variant_text_sha256': digest(html['text'].encode())}
    except Exception as exc:
        checks['html_processing'] = {'status': 'failed', 'error': str(exc)}
        if args.baseline:
            report['content_fidelity'] = {'status': 'failed', 'error': str(exc)}
    doc = None
    try:
        doc = fitz.open(args.pdf)
        if not doc.is_pdf or doc.needs_pass or not len(doc):
            raise ValueError('Input must be a readable, non-empty, unencrypted PDF')
        checks['pdf_valid'] = {'status': 'passed', 'pages': len(doc)}
        dimensions = [[round(p.rect.width, 2), round(p.rect.height, 2)] for p in doc]
        a4 = all(abs(sorted(d)[0] - 595.276) <= 2 and abs(sorted(d)[1] - 841.89) <= 2 for d in dimensions)
        checks['pdf_a4'] = {'status': 'passed' if a4 else 'failed', 'page_dimensions_points': dimensions, 'tolerance_points': 2}
        author = doc.metadata.get('author', '')
        checks['pdf_author'] = {'status': 'passed' if author == args.author else 'failed', 'actual': author, 'expected': args.author}
        checks['pdf_page_count'] = {'status': 'not_checked' if args.expect_pages is None else ('passed' if len(doc) == args.expect_pages else 'failed'), 'actual': len(doc), 'expected': args.expect_pages}
        residuals = []
        text_sizes = []
        for index, page in enumerate(doc, 1):
            text = page.get_text()
            text_sizes.append(len(text))
            residuals.extend({'page': index, 'match': m.group(0)} for m in TEX_RE.finditer(text))
        checks['pdf_tex_residuals'] = {'status': 'failed' if residuals else 'passed', 'matches': residuals, 'extracted_characters_per_page': text_sizes,
                                     'scope': 'Obvious command-pattern scan of extractable PDF text only; no OCR'}
        if not any(text_sizes):
            checks['pdf_tex_residuals'].update(status='not_checked', reason='No extractable text; OCR was not performed')
        toc = doc.get_toc()
        checks['pdf_outline'] = {'status': 'passed' if toc else ('failed' if args.require_outline else 'not_checked'), 'required': args.require_outline, 'entries': toc,
                                 'target_page_validation': 'not_checked'}
        if args.expected_outline:
            expected = json.loads(args.expected_outline.read_text(encoding='utf-8'))
            wanted = list(expected.items()) if isinstance(expected, dict) else [(i['title'], i['page']) for i in expected]
            if not wanted or any(not isinstance(t, str) or not isinstance(p, int) or p < 1 or p > len(doc) for t, p in wanted):
                raise ValueError('expected-outline requires nonempty title/page pairs with valid one-based pages')
            actual = [(item[1], item[2]) for item in toc]
            checks['pdf_outline_expected'] = compare_lists(wanted, actual)
            checks['pdf_outline_expected'].update({'expected': wanted, 'actual': actual, 'scope': 'Exact title/page/order against supplied expectation; does not validate printed TOC or clicks'})
            checks['pdf_outline']['target_page_validation'] = 'checked_against_supplied_expectation'
        if args.preview_dir:
            args.preview_dir.mkdir(parents=True, exist_ok=True)
            paths = []
            thumbs = []
            for index, page in enumerate(doc, 1):
                pix = page.get_pixmap(matrix=fitz.Matrix(1, 1), alpha=False)
                out = args.preview_dir / f'page-{index:03d}.png'
                pix.save(str(out))
                paths.append(str(out.resolve()))
                thumbs.append(page.get_pixmap(matrix=fitz.Matrix(0.30, 0.30), alpha=False))
            cols = min(4, len(thumbs))
            cell_w = max(p.width for p in thumbs) + 12
            cell_h = max(p.height for p in thumbs) + 12
            sheet = fitz.open()
            for start in range(0, len(thumbs), 24):
                batch = thumbs[start:start + 24]
                canvas = sheet.new_page(width=cols * cell_w, height=((len(batch) + cols - 1) // cols) * cell_h)
                for n, pix in enumerate(batch):
                    x, y = (n % cols) * cell_w + 6, (n // cols) * cell_h + 6
                    canvas.insert_image(fitz.Rect(x, y, x + pix.width, y + pix.height), pixmap=pix)
                name = 'contact.jpg' if start == 0 else f'contact-{start // 24 + 1:03d}.jpg'
                out = args.preview_dir / name
                canvas.get_pixmap(alpha=False).save(str(out))
                paths.append(str(out.resolve()))
            sheet.close()
            report['previews'] = {'status': 'generated_not_reviewed', 'dpi': 72, 'files': paths}
    except Exception as exc:
        checks['pdf_processing'] = {'status': 'failed', 'error': str(exc)}
    finally:
        if doc is not None:
            doc.close()
    failed = any(c.get('status') == 'failed' for c in checks.values()) or report['content_fidelity']['status'] == 'failed'
    report['overall_status'] = 'failed' if failed else 'machine_checks_passed'
    report['completion_scope'] = 'Machine checks only; see individual not_checked and not_performed fields'
    args.report.parent.mkdir(parents=True, exist_ok=True)
    try:
        with args.report.open('w' if args.replace else 'x', encoding='utf-8') as handle:
            json.dump(report, handle, ensure_ascii=False, indent=2)
            handle.write('\n')
    except OSError as exc:
        print(f'Cannot write report: {exc}', file=sys.stderr)
        return 2
    print(f"{report['overall_status']}: {args.report}")
    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main())
