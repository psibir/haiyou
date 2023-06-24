import unittest
from io import StringIO
from unittest.mock import patch
from ..haiyou import HaikuValidator, HaikuStructureError

class HaikuValidatorTestCase(unittest.TestCase):
    def test_valid_haiku(self):
        haiku = "An old silent pond\nA frog jumps into the pond—\nSplash! Silence again."
        validator = HaikuValidator(haiku)
        self.assertTrue(validator.validate_haiku())

    def test_invalid_haiku(self):
        haiku = "An old silent pond\nA frog jumps into the pond—\nSplash!"
        validator = HaikuValidator(haiku)
        with self.assertRaises(HaikuStructureError):
            validator.validate_haiku()

class MainTestCase(unittest.TestCase):
    @patch('builtins.input', side_effect=['An old silent pond', 'en'])
    def test_main_valid_haiku(self, mock_input):
        expected_output = "Valid haiku!"
        with patch('sys.stdout', new=StringIO()) as fake_output:
            main()
            self.assertEqual(fake_output.getvalue().strip(), expected_output)

    @patch('builtins.input', side_effect=['An old silent pond', 'fr'])
    def test_main_invalid_haiku(self, mock_input):
        expected_output = "Invalid haiku:\nHaiku must have exactly 3 lines."
        with patch('sys.stdout', new=StringIO()) as fake_output:
            main()
            self.assertEqual(fake_output.getvalue().strip(), expected_output)

if __name__ == '__main__':
    unittest.main()
