import unittest
from unittest.mock import patch
from io import StringIO
import os

from find import word_search


class TestWordSearchFunctional(unittest.TestCase):

    @patch("sys.stdout", new_callable=StringIO)
    @patch("sys.argv", ["find.py", "test.txt", "lithuania"])
    def test_word_search_functional(self, mock_stdout):
        """
        Tests the word_search function in a functional manner.
        """
        with open("test.txt", "w") as f:
            f.write("Lithuania is a beautiful country. Welcome to Lithuania!")

        word_search()
        output = mock_stdout.getvalue()

        self.assertIn("Lithuania", output)
        self.assertIn("country", output)

        if os.path.exists("test.txt"):
            os.remove("test.txt")


if __name__ == "__main__":
    unittest.main()
