import argparse

import re
import pandas as pd

from utils.soundex import Soundex
from utils.processing import process_file, create_df, preprocess_df, clustering

# Initialize the Soundex algorithm for encoding words
algorithm = Soundex()


def word_search():
    """
    Searches for the top 5 matched words in a given text file based on the provided word.
    """
    parser = argparse.ArgumentParser(
        description="Find top 5 matched words from a given text file."
    )
    parser.add_argument("file", help="The path to the text file.")
    parser.add_argument("word", help="The word to match.")

    args = parser.parse_args()

    # Process the content of the text file and extract words
    content = process_file(args.file)

    # Create a DataFrame with words and their Soundex encodings
    df = create_df(content, algorithm)

    # Preprocess the DataFrame by encoding the letters and numbers (for clustering)
    df_preprocessed = preprocess_df(df)

    # Encode the input word using the Soundex algorithm
    input_code = algorithm.encode(args.word)

    # Perform clustering to find the top matches for the input Soundex code
    top_matches = clustering(df_preprocessed, input_code)
    print(top_matches)

    return


if __name__ == "__main__":
    word_search()
