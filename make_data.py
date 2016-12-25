#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
http://www.histdata.com/download-free-forex-data/
"""
import pandas as pd
import re


def read_metatrader(infile):
    columns = ['day', 'time', 'open', 'high', 'low', 'close', 'volume']
    df = pd.read_csv(infile, names=columns, usecols=[0, 1, 5])
    df.index = pd.to_datetime((df['day'] + ' ' + df['time']))
    return df.drop(['day', 'time'], 1)


def interpolate(df):
    return df.resample('T').pad()


def transform(infile):
    df = read_metatrader(infile)
    df = interpolate(df)
    outfile = re.sub('.csv$', '.clean.csv', infile)
    print('writing ' + outfile)
    df.to_csv(outfile, header=False)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('infile')
    args = parser.parse_args()
    transform(args.infile)
