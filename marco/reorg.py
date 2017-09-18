#!/usr/bin/env python

import csv
import argparse

parser = argparse.ArgumentParser(
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    description='Play with data from Marco to show off Python.')

parser.add_argument(
    'csvFile', help='The CSV data file to open.')

parser.add_argument(
    '--printHeader', default=False, action='store_true',
    help='If specified, print a CSV header line.')

args = parser.parse_args()

firstRow = True
newId = 0

with open(args.csvFile, newline='') as csvfile:
    for row in csv.reader(csvfile):
        if firstRow:
            if args.printHeader:
                print(','.join(row[0:10]))
            firstRow = False
        else:
            (origId, emptyColumn, date, dayOrNight, species,
             count, sex, trapPoint, trapType, comments) = row[0:10]
            assert emptyColumn == ''

            count = int(count)

            for _ in range(count):
                newId += 1
                print(','.join([
                    origId, str(newId), date, dayOrNight, species,
                      '1', sex, trapPoint, trapType, comments]))
