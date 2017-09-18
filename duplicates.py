import sys

seen = set()

for line in sys.stdin:
    if line.startswith('>'):
        if line in seen:
            print('Already seen', line)
        seen.add(line)
