#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
http://www.histdata.com/download-free-forex-data/
"""
import pandas as pd
import numpy as np
import re
import os


def read_metatrader(infile):
    columns = ['day', 'time', 'open', 'high', 'low', 'close', 'volume']
    df = pd.read_csv(infile, names=columns, usecols=[0, 1, 5])
    df.index = pd.to_datetime((df['day'] + ' ' + df['time']))
    return df.drop(['day', 'time'], 1)


def interpolate(df):
    return df.resample('T').pad()


def extract(df, i, n, m, d):
    x = df.iloc[(i - n):i, 0].values
    current = df.iat[i, 0]
    future = df.iat[i + m, 0]
    if future < current - d:
        t = [1, 0, 0]
    elif current + d < future:
        t = [0, 0, 1]
    else:
        t = [0, 1, 0]
    return (x, np.array(t))


def sample(df, size, n=200, m=5, d=0.03):
    indices = np.random.randint(n, len(df) - 5, size)
    xlist = []
    tlist = []
    for i in indices:
        (x, t) = extract(df, i, n, m, d)
        xlist.append(x)
        tlist.append(t)
    return (np.vstack(xlist), np.vstack(tlist))


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--length', type=int, default=200)
    parser.add_argument('-m', '--gap', type=int, default=5)
    parser.add_argument('-d', '--threshold', type=float, default=0.03)
    parser.add_argument('-N', '--samplesize', type=int, default=1000)
    parser.add_argument('infile')
    args = parser.parse_args()

    df = read_metatrader(args.infile)
    df = interpolate(df)
    (x, t) = sample(df, args.samplesize, args.length, args.gap, args.threshold)

    infile = os.path.basename(args.infile)
    xoutfile = re.sub('.csv$', '.x.csv.gz', infile)
    toutfile = re.sub('.csv$', '.t.csv.gz', infile)
    print('writing ' + xoutfile)
    np.savetxt(xoutfile, x, delimiter=',', fmt='%.6f')
    print('writing ' + toutfile)
    np.savetxt(toutfile, t, delimiter=',', fmt='%d')
