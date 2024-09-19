# oxylabs-task: Word Search

Implement a CLI tool that finds top 5 matched words from a given text file, using the American Soundex algorithm to match the words.

## American Soundex algorithm steps (from [Soundex - Wikipedia][https://en.wikipedia.org/wiki/Soundex])

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