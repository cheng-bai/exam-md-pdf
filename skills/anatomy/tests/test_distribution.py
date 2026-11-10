import unittest
from pathlib import Path


class DistributionTests(unittest.TestCase):
    def test_required_math_resources_are_packaged(self):
        root = Path(__file__).resolve().parents[1]
        required = (
            "references/math-teaching.md",
            "references/math-design.md",
            "references/math-validation.md",
            "references/feedback-regression.md",
            "references/resource-package.md",
            "references/question-bindings.md",
            "scripts/resources.py",
            "scripts/question_bindings.py",
            "scripts/inline-kit.mjs",
            "scripts/capture.mjs",
            "scripts/drive.mjs",
            "examples/math-tetrahedron/CONCEPT.md",
            "examples/math-tetrahedron/model.mjs",
            "examples/math-tetrahedron/check.mjs",
            "examples/math-tetrahedron/build.mjs",
            "examples/math-tetrahedron/package.mjs",
            "examples/math-tetrahedron/scenes.json",
            "examples/math-tetrahedron/state-contract.json",
        )
        missing = [name for name in required if not (root / name).is_file()]
        self.assertEqual(missing, [])

    def test_skill_links_to_feedback_workflow(self):
        root = Path(__file__).resolve().parents[1]
        skill = (root / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("(references/feedback-regression.md)", skill)


if __name__ == "__main__":
    unittest.main()
