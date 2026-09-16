import importlib.util
from pathlib import Path
import tempfile
import unittest

SPEC = importlib.util.spec_from_file_location('validator', Path(__file__).resolve().parents[1] / 'scripts/validate.py')
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class PackagingValidationTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.skill = self.root / 'skills/sample'
        self.skill.mkdir(parents=True)
        self.entry = self.skill / 'SKILL.md'
        self.entry.write_text('---\nname: sample\ndescription: Sample workflow\n---\n\n# Sample\n')

    def test_portable_skill_with_reference(self):
        (self.skill / 'references').mkdir()
        (self.skill / 'references/detail.md').write_text('# Detail\n')
        with self.entry.open('a') as stream:
            stream.write('[Details](references/detail.md)\n')
        self.assertEqual(VALIDATOR.validate(self.root), [])

    def test_missing_supporting_file_fails(self):
        with self.entry.open('a') as stream:
            stream.write('[Details](references/missing.md)\n')
        self.assertTrue(any('missing linked file' in error for error in VALIDATOR.validate(self.root)))

    def test_mismatched_discovery_name_fails(self):
        self.entry.write_text(self.entry.read_text().replace('name: sample', 'name: renamed'))
        self.assertTrue(any('name must match' in error for error in VALIDATOR.validate(self.root)))

    def test_nonmapping_yaml_fails_cleanly(self):
        self.entry.write_text('---\n- not-a-mapping\n---\n# Example\n')
        self.assertTrue(any('must be a mapping' in error for error in VALIDATOR.validate(self.root)))

    def test_external_file_dependency_fails(self):
        with self.entry.open('a') as stream:
            stream.write('[Private file](../../../private.md)\n')
        self.assertTrue(any('escapes repository' in error for error in VALIDATOR.validate(self.root)))


if __name__ == '__main__':
    unittest.main()
