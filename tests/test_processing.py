import unittest
import pandas as pd
import os

from utils.processing import process_file, create_df, preprocess_df
from utils.soundex import Soundex


class TestProcessing(unittest.TestCase):

    def setUp(self):
        self.soundex = Soundex()

    def test_process_file(self):
        """
        Tests the process_file function by creating a test file, writing content to it,
        processing the file, and asserting the result matches the expected output.
        """
        content = "Hello oxylabs! Welcome to testing."
        with open("test.txt", "w") as f:
            f.write(content)
        result = process_file("test.txt")
        self.assertEqual(result, ["Hello", "oxylabs", "Welcome", "to", "testing"])

        if os.path.exists("test.txt"):
            os.remove("test.txt")

    def test_create_df(self):
        """
        Tests the creation of a DataFrame from a list of words using the create_df function.

        Verifies that the resulting DataFrame is an instance of pd.DataFrame and has the correct number of rows.
        """
        words = ["Hello", "oxylabs", "testing"]
        df = create_df(words, self.soundex)
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertEqual(len(df), 3)  # Should have 3 rows

    def test_preprocess_df(self):
        """
        Test the preprocess_df function by creating a DataFrame from a list of words,
        preprocessing the DataFrame, and asserting that the resulting DataFrame has a
        column named "letter_encoded".
        """
        words = ["Hello", "oxylabs", "testing"]
        df = create_df(words, self.soundex)
        df_preprocessed = preprocess_df(df)
        self.assertIn("letter_encoded", df_preprocessed.columns)


if __name__ == "__main__":
    unittest.main()
