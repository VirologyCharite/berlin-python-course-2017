import sys

# The 'counts' dict will hold the count for each letter seen on input.
counts = {}

for line in sys.stdin:
    for letter in line.lower():

        if letter.isalpha():
            if letter in counts:
                counts[letter] += 1
            else:
                counts[letter] = 1

for letter in counts:
    print(counts[letter], letter)
