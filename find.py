import argparse

import re
import pandas as pd

from utils.soundex import Soundex
from utils.processing import process_file, create_df, preprocess_df, clustering

algorithm = Soundex()


def word_search():
    parser = argparse.ArgumentParser(
        description="Find top 5 matched words from a given text file."
    )
    parser.add_argument("file", help="The path to the text file.")
    parser.add_argument("word", help="The word to match.")

    args = parser.parse_args()

    content = process_file(args.file)
    df = create_df(content, algorithm)
    df_preprocessed = preprocess_df(df)

    input_code = algorithm.encode(args.word)

    closest = clustering(df_preprocessed, input_code)
    print(closest)

    return


if __name__ == "__main__":
    word_search()
