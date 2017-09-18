#!/usr/bin/env python

"""
This script counts the number of sequences in a FASTA file given
on standard input. The result is printed to standard output.
"""

import sys

count = 0

for line in sys.stdin:
    if line.startswith('>'):
        count = count + 1

print(count)
