import unittest
from utils.soundex import Soundex

names = [
    "Gough",
    "O'Conner",
    "Ashcroft",
    "Tymczak",
    "Pfister",
    "Honeyman",
    "Tchaikovsky",
]
codes = ["G200", "O256", "A261", "T522", "P236", "H555", "T221"]


class TestSoundex(unittest.TestCase):

    def setUp(self):
        self.soundex = Soundex()

    def test_encode_basic_word(self):
        """Test case for the `encode` method of the `Soundex` class with a basic word."""
        self.assertEqual(self.soundex.encode("example"), "E251")

    def test_encode_with_numbers(self):
        """Test case for the `encode` method of the `Soundex` class when input contains numbers."""
        self.assertEqual(self.soundex.encode("123abc"), "A120")

    def test_encode_empty_string(self):
        """Test case for the `encode` method of the `Soundex` class when the input is an empty string."""
        self.assertIsNone(self.soundex.encode(""))

    def test_encode_with_special_characters(self):
        """Test case for the `encode` method of the `Soundex` class when input contains special characters."""
        self.assertEqual(self.soundex.encode("lithuania!!"), "L350")

    def test_encode_hard_cases(self):
        """Test case for the `encode` method of the `Soundex` class with hard cases."""
        self.assertEqual(self.soundex.encode("lithuania"), "L350")
        for name, code in zip(names, codes):
            self.assertEqual(
                self.soundex.encode(name), code
            ), f"{self.soundex.encode(name)} != {code}"


if __name__ == "__main__":
    unittest.main()
