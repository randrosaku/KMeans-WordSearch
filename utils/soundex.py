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

alphabet = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"


class Soundex:

    def __init__(self, tbl: dict = tbl):
        self.tbl = tbl
        self.word = None

    def encode(self, input_word: str, tbl: dict = tbl) -> str:
        self.word = "".join([char for char in input_word if char in alphabet])

        if not self.word:
            return None

        first_letter = self.word[0].upper()
        translation = self.word.lower().translate(tbl)

        result_seq = []
        for i in range(1, len(translation)):
            if i == 1 and translation[i] == first_letter.lower().translate(tbl):
                continue
            elif translation[i] in "yhw":
                if i == len(self.word) - 1:
                    continue
                if result_seq and translation[i + 1] == result_seq[-1]:
                    result_seq.pop()
            else:
                if not result_seq or translation[i] != result_seq[-1]:
                    result_seq.append(translation[i])

        result = "".join(result_seq).replace("0", "")

        return first_letter + (result + "000")[:3]
