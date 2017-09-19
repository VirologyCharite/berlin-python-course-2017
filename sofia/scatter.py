#!/usr/bin/env python

import csv
import argparse
import plotly
from plotly.graph_objs import Layout, Scatter

parser = argparse.ArgumentParser(
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    description='Read Sofia csv and make a scatter plot')

parser.add_argument(
    '--csv', required=True, help='The CSV file to open.')

parser.add_argument(
    '--header', default=False, action='store_true',
    help='If True, read (and ignore) one header line.')

args = parser.parse_args()


def getData(filename):
    firstRow = True
    x = []
    y = []
    comments = []

    with open(filename, newline='', encoding='iso-8859-1') as csvfile:
        for row in csv.reader(csvfile):
            if args.header and firstRow:
                firstRow = False
            else:
                x.append(float(row[0]))
                y.append(float(row[1]))
                comments.append(row[2])

    return x, y, comments


def makePlot(x, y, comments):
    layout = Layout(
        title='title',
        font={
            'family': 'Helvetica',
            'size': 12,
        },
        xaxis={
            'title': 'X title',
        },
        yaxis={
            'title': 'Y title',
        },
        hovermode='closest',
    )

    plotly.offline.plot({
        'data': [Scatter(x=x, y=y, mode='markers', text=comments)],
        'layout': layout,
    })


x, y, comments = getData(args.csv)
makePlot(x, y, comments)
