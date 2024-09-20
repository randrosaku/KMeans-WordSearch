import re
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

from utils.soundex import Soundex


def read_file(file: str) -> str:
    file = open(file, "r", encoding="utf-8")
    content = file.read()
    file.close()

    return content


def process_file(file: str) -> str:
    content = read_file(file)

    clean_content = content.replace("\n", " ")
    words = re.findall(r"\b\w+\b", clean_content)

    return words


def create_df(content: list, algorithm: Soundex) -> pd.DataFrame:

    codes = []
    words = []

    for word in content:
        code = algorithm.encode(word)
        if code:
            codes.append(code)
            words.append(algorithm.word)

    df = pd.DataFrame(list(zip(codes, words)), columns=["code", "word"])

    return df


def extract_letters_and_numbers(text):
    return text[0], int(text[1:])


def preprocess_df(df):
    df["letter"], df["numbers"] = zip(*df["code"].apply(extract_letters_and_numbers))
    df["letter_encoded"] = df["letter"].apply(lambda x: ord(x) if x else 0)

    return df


def clustering(df, input_code):
    X = df[["letter_encoded", "numbers"]]

    kmeans = KMeans(n_clusters=5, random_state=42)
    kmeans.fit(X)

    return
