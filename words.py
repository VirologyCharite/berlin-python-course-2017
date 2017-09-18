import sys

# The 'counts' dict will hold the count for each word seen on input.
counts = {}

totalWords = 0
uniqueWords = 0

for line in sys.stdin:
    words = line.split()
    totalWords += len(words)

    for word in words:
        if word in counts:
            counts[word] += 1
            # counts[word] = counts[word] + 1
        else:
            counts[word] = 1
            uniqueWords += 1

print('There were', totalWords, 'words in total, and',
      uniqueWords, 'unique words.')

for word in counts:
    print(counts[word], word)
