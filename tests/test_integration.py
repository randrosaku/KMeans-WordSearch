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

        # Read and process text file
        processed_words = process_file("integration_test.txt")

        # Create and process DataFrame
        df_chunks = list(create_df(processed_words, self.soundex))
        df = pd.concat(df_chunks, ignore_index=True)
        df_preprocessed = preprocess_df(df)

        # Test Soundex encoding
        input_code = self.soundex.encode("lithuania")

        # Perform KMeans clustering
        top_matches = clustering(df_preprocessed, input_code)
        top_matches_lower = [word.lower() for word in top_matches]

        # Check that top matches contain expected word
        self.assertIn("lithuania".lower(), top_matches_lower)

        if os.path.exists("integration_test.txt"):
            os.remove("integration_test.txt")


if __name__ == "__main__":
    unittest.main()
