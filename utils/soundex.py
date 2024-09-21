tbl = str.maketrans(
    {
        "a": "0",
        "e": "0",
        "i": "0",
        "o": "0",
        "u": "0",
        "b": "1",
        "f": "1",
        "p": "1",
        "v": "1",
        "c": "2",
        "g": "2",
        "j": "2",
        "k": "2",
        "q": "2",
        "s": "2",
        "x": "2",
        "z": "2",
        "d": "3",
        "t": "3",
        "l": "4",
        "m": "5",
        "n": "5",
        "r": "6",
    }
)

# Define the alphabet, including lowercase and uppercase letters, for filtering valid characters
alphabet = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"


class Soundex:
    """This class implements the American Soundex algorithm for encoding words."""

    def __init__(self, tbl: dict = tbl):
        """
        Initializes a Soundex object with a translation table and an optional word.

        Parameters:
            tbl (dict): A dictionary mapping characters to their corresponding Soundex codes.

        Returns:
            None
        """
        self.tbl = tbl
        self.word = None

    def encode(self, input_word: str, tbl: dict = tbl) -> str:
        """
        Encodes a given word using the Soundex algorithm.

        Parameters:
            input_word (str): The word to encode.
            tbl (dict, optional): A dictionary mapping characters to their corresponding Soundex codes. Defaults to the predefined tbl.

        Returns:
            str: The encoded word, or None if the input_word is empty.
        """
        # Filter out any characters from the input_word that are not part of the alphabet
        self.word = "".join([char for char in input_word if char in alphabet])

        if not self.word:
            return None

        # Retain the first letter (in uppercase) for the Soundex code
        first_letter = self.word[0].upper()

        # Convert the rest of the word to its Soundex encoded form using the translation table
        translation = self.word.lower().translate(tbl)

        result_seq = []
        for i in range(1, len(translation)):
            if i == 1 and translation[i] == first_letter.lower().translate(tbl):
                continue
            # Handle 'y', 'h', 'w' as per Soundex rules
            elif translation[i] in "yhw":
                if i == len(self.word) - 1:
                    continue
                if result_seq and translation[i + 1] == result_seq[-1]:
                    result_seq.pop()
            else:
                if not result_seq or translation[i] != result_seq[-1]:
                    result_seq.append(translation[i])

        # Remove all '0' values (which represent ignored letters) and pad/truncate the result to 3 digits
        numeric_part = "".join(result_seq).replace("0", "")
        soundex_code = first_letter + (numeric_part + "000")[:3]

        return soundex_code
