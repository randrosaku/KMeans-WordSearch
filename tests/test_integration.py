import unittest
import pandas as pd
import os

from utils.soundex import Soundex
from utils.processing import process_file, create_df, preprocess_df, clustering


class TestIntegration(unittest.TestCase):

    def setUp(self):
        self.soundex = Soundex()

    def test_full_integration(self):
        content = "Lithuania is a beautiful country. Welcome to Lithuania!"
        with open("integration_test.txt", "w") as f:
            f.write(content)

        # Process the file
        processed_words = process_file("integration_test.txt")

        # Create and process DataFrame
        df = create_df(processed_words, self.soundex)
        df_preprocessed = preprocess_df(df)

        # Test Soundex encoding for a specific word
        input_code = self.soundex.encode("lithuania")

        # Perform clustering
        top_matches = clustering(df_preprocessed, input_code)
        top_matches_lower = [word.lower() for word in top_matches.values]

        # Check that top matches contain expected words
        self.assertIn("lithuania".lower(), top_matches_lower)

        if os.path.exists("integration_test.txt"):
            os.remove("integration_test.txt")


if __name__ == "__main__":
    unittest.main()
