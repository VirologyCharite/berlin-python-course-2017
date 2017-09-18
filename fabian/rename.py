#!/usr/bin/env python

import sys
import csv
import argparse
from Bio import SeqIO

parser = argparse.ArgumentParser(
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    description='Play with data from Marco to show off Python.')

parser.add_argument(
    '--csv', required=True, help='The CSV file to open.')

parser.add_argument(
    '--fasta', required=True, help='The FASTA file to open.')

# parser.add_argument(
#     '--printHeader', default=False, action='store_true'
#     help='If specified, print a CSV header line.')

args = parser.parse_args()

# print('FASTA is', args.fasta, 'Csv is', args.csv)

# Read the FASTA file and store it into a dictionary.

fasta = {}
for record in SeqIO.parse(args.fasta, 'fasta'):
    fasta[record.id] = str(record.seq)

# Read the CSV.

firstRow = True
missingIds = set()

with open(args.csv, newline='', encoding='iso-8859-1') as csvfile:
    for row in csv.reader(csvfile):
        if firstRow:
            firstRow = False
        else:
            sampleId = row[1]
            species = row[2]

            if sampleId and species:
                if sampleId in fasta:
                    print('>PN_%s_%s' % (sampleId, species))
                    print(fasta[sampleId])
                else:
                    missingIds.add(sampleId)
            else:
                if not all(cell == '' for cell in row):
                    print('Ignoring line', ' '.join(row),
                          file=sys.stderr)

if missingIds:
    print('The following ids were not found in', args.fasta,
          missingIds, file=sys.stderr)
