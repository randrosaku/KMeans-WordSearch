import re
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

from utils.soundex import Soundex


def read_file(file: str) -> str:
    """
    Reads the contents of a file and returns it as a string.

    Parameters:
        file (str): The path to the file to be read.

    Returns:
        str: The contents of the file.
    """
    file = open(file, "r", encoding="utf-8")
    content = file.read()
    file.close()

    return content


def process_file(file: str) -> list:
    """
    Processes a given file by reading its contents, cleaning the text, and extracting individual words.

    Parameters:
        file (str): The path to the file to be processed.

    Returns:
        list: A list of words extracted from the file.
    """
    content = read_file(file)

    clean_content = content.replace("\n", " ")
    words = re.findall(r"\b\w+\b", clean_content)

    return words


def create_df(content: list, algorithm: Soundex) -> pd.DataFrame:
    """
    Creates a DataFrame from a list of words and their corresponding Soundex codes.

    Parameters:
        content (list): A list of words to be encoded.
        algorithm (Soundex): An instance of the Soundex class.

    Returns:
        pd.DataFrame: A DataFrame containing the encoded words and their corresponding Soundex codes.
    """
    codes = []
    words = []

    for word in content:
        code = algorithm.encode(word)
        if code:
            codes.append(code)
            words.append(algorithm.word)

    df = pd.DataFrame(list(zip(codes, words)), columns=["code", "word"])

    return df


def extract_letters_and_numbers(text: str) -> tuple:
    """
    Extracts the first letter and the remaining numbers from a given string.

    Parameters:
        text (str): The Soundex code containing a letter followed by numbers.

    Returns:
        tuple: A tuple containing the first letter as a string and the remaining numbers as an integer.
    """
    return text[0], int(text[1:])


def preprocess_df(df: pd.DataFrame) -> pd.DataFrame:
    """
    Preprocesses a DataFrame by encoding the letter with ASCII and the remaining numbers.

    Parameters:
        df (pd.DataFrame): The DataFrame to be preprocessed.

    Returns:
        pd.DataFrame: The preprocessed DataFrame.
    """
    df["letter"], df["numbers"] = zip(*df["code"].apply(extract_letters_and_numbers))
    df["letter_encoded"] = df["letter"].apply(lambda x: ord(x) if x else 0)

    return df


def adaptive_k(
    X: pd.DataFrame,
    df: pd.DataFrame,
    initial_k: int = 5,
    min_cluster_size: int = 5,
    min_k: int = 2,
) -> KMeans:
    """
    This function performs adaptive clustering using KMeans algorithm.

    Parameters:
        X (pd.DataFrame): The input DataFrame for clustering.
        df (pd.DataFrame): The DataFrame to assign cluster labels to.
        initial_k (int, optional): The initial number of clusters. Defaults to 5.
        min_cluster_size (int, optional): The minimum size of a cluster. Defaults to 5.
        min_k (int, optional): The minimum number of clusters to consider. Defaults to 2.

    Returns:
        KMeans: The KMeans object with the optimal clustering.
    """
    k = initial_k

    while k >= min_k:
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(X)

        labels, counts = np.unique(kmeans.labels_, return_counts=True)

        if all(count >= min_cluster_size for count in counts):
            df["cluster"] = kmeans.labels_
            return kmeans

        k -= 1

    df["cluster"] = kmeans.labels_
    return kmeans


def distance(
    input_encoded: np.ndarray, cluster_codes_encoded: np.ndarray
) -> np.ndarray:
    """
    Calculate the distance between an input encoded value and a set of cluster codes encoded values.

    Parameters:
        input_encoded (np.ndarray): The input encoded value.
        cluster_codes_encoded (np.ndarray): The encoded values of the cluster codes.

    Returns:
        np.ndarray: The calculated distance between the input encoded value and the cluster codes encoded values, preferring letters.
    """
    input_letter, input_numbers = input_encoded[0], input_encoded[1]

    cluster_letters = cluster_codes_encoded[:, 0]
    cluster_numbers = cluster_codes_encoded[:, 1]

    letter_distances = np.abs(cluster_letters - input_letter)
    number_distances = np.abs(cluster_numbers - input_numbers)

    return letter_distances * 10 + number_distances


def find_similar(
    input: str, kmeans: KMeans, df: pd.DataFrame, num_closest: int = 5
) -> pd.DataFrame:
    """
    Find the top `num_closest` similar words from a given DataFrame based on the input word.

    Parameters:
        input (str): The input word to find similar words for.
        kmeans (KMeans): The KMeans object used for clustering.
        df (pd.DataFrame): The DataFrame containing the words and their cluster labels.
        num_closest (int, optional): The number of top similar words to return. Defaults to 5.

    Returns:
        pd.DataFrame: The top `num_closest` similar words from the DataFrame.
    """
    input_letter, input_numbers = extract_letters_and_numbers(input)
    input_letter_encoded = ord(input_letter) if input_letter else 0

    input_encoded = np.array([[input_letter_encoded, input_numbers]])

    predicted_cluster = kmeans.predict(input_encoded)[0]

    cluster = df[df["cluster"] == predicted_cluster]
    cluster_codes_encoded = cluster[["letter_encoded", "numbers"]].values

    distances = distance(input_encoded[0], cluster_codes_encoded)
    closest_indices = np.argsort(distances)[:num_closest]

    return cluster.iloc[closest_indices]


def clustering(df: pd.DataFrame, input_code: str) -> list:
    """
    Rerforms clustering on a given DataFrame to find the top matches based on the Soundex-encoded word.

    Parameters:
        df (pd.DataFrame): The DataFrame containing the words and their features.
        input_code (str): The input code used for clustering.

    Returns:
        list: A list of the top matches found in the DataFrame.
    """
    X = df[["letter_encoded", "numbers"]]
    kmeans = adaptive_k(X, df)

    closest_codes = find_similar(input_code, kmeans, df)

    return closest_codes["word"]
