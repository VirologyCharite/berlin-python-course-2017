import sys

count = 0

for line in sys.stdin:
    if line.startswith('>'):
        count = count + 1

print(count)
