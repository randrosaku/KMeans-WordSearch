# Word Search

This project implements a CLI tool that allows users to find the top 5 words from a given text file that match a target word based on the American Soundex algorithm. The Soundex algorithm is used to map words with similar pronunciation to the same encoded value, enabling phonetic matching.

This tool is particularly useful for tasks such as text matching where spelling variations occur but the pronunciation remains similar. It uses the scikit-learn library for clustering similar words based on their Soundex codes and their ASCII encoded features.

## Setup Instructions

### 1. Install Anaconda/Miniconda (if not installed)
Ensure that you have Conda installed on your system. You can install either [Anaconda](https://www.anaconda.com/products/individual) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html) depending on your preference.

### 2. Create a development environment

In the project directory, run the following command to create a Conda environment with the required dependencies:
```
conda env create -f environment.yml
```
### 3. Activate the environment
Activate the newly created environment using:
```
conda activate oxylabs
```
### 4. Run the CLI Tool
You can now run the tool to find the top matches from a text file based on the Soundex algorithm. Use the following command:
```
./find.py file_path word_to_match
```
Replace `file_path` with the path to your text file and `word_to_match` with the word you're searching for.

**Example**
```
./find.py wiki_lt.txt lithuania
```
This command will search for the top 5 phonetic matches to the word "lithuania" in the wiki_lt.txt file, based on American Soundex algorithm.

## Algorithm Details
The tool uses the American Soundex algorithm to encode words phonetically and match words that sound similar. Below are the steps of the algorithm (based on [Soundex - Wikipedia](https://en.wikipedia.org/wiki/Soundex))

1. Retain the first letter of the name and drop all other occurrences of a, e, i, o, u, y, h, w.
2. Replace consonants with digits as follows (after the first letter):
    * b, f, p, v → 1
    * c, g, j, k, q, s, x, z → 2
    * d, t → 3
    * l → 4
    * m, n → 5
    * r → 6
3. If two or more letters with the same number are adjacent in the original name (before step 1), only retain the first letter; also two letters with the same number separated by 'h', 'w' or 'y' are coded as a single number, whereas such letters separated by a vowel are coded twice. This rule also applies to the first letter.
4. If there are too few letters in the word to assign three numbers, append zeros until there are three numbers. If there are four or more numbers, retain only the first three.

## Dependencies and Tools

The project uses the following libraries and tools:

### Python Libraries:
- `pandas`: Used for handling data structures.
- `pydantic`: Provides data validation and settings management.
- `numpy`: Utilized for numerical operations.
- `scikit-learn`: Implements machine learning algorithms (used here for clustering similar words).
- `argparse`: Used to handle the command-line interface and argument parsing.

### Environment Setup:
All dependencies can be installed via the `conda` package manager. The `environment.yml` file specifies the necessary libraries and tools for the project.

### Development Tools:
- **Anaconda/Miniconda**: Used for environment management.
- **Python 3.10**: The project requires Python version 3.10 or higher.
---

&copy; Rasa Kundrotaite
