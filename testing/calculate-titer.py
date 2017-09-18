#!/usr/bin/env python

import argparse

from plaques import calculateTiter

parser = argparse.ArgumentParser(
    description=('Calculate a titer from plaque counts, dilutions, '
                 'and a volume'))

parser.add_argument(
    '--counts', required=True, type=int, nargs='+', help='The plaque counts')

parser.add_argument(
    '--dilutions', required=True, type=int, nargs='+', help='The dilutions')

parser.add_argument(
    '--volume', required=True, type=int, help='The volume')

args = parser.parse_args()

print(calculateTiter(args.counts, args.dilutions, args.volume))
