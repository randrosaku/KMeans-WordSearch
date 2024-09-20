from utils.soundex import Soundex

algorithm = Soundex()

code = algorithm.encode("Lithu??ania*//>", tbl=algorithm.tbl)

print(code)
print(algorithm.word)
