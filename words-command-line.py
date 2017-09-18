from sys import argv, exit

if len(argv) == 2:
    filename = argv[1]
else:
    print('I need exactly one filename!')
    exit()

# The 'counts' dict will hold the count for each word seen on input.
counts = {}

totalWords = 0
uniqueWords = 0

for line in open(filename):
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
