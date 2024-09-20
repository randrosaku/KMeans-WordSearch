import re
import pandas as pd

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
