#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

from mpltools import style

style.use('ggplot')

graphs = [
    'baseline',
    'put',
    'list',
    'flag',
    'get',
    'delete',
]


def get_data():
    data = {}
    with open('results.txt') as f:
        for line in f.readlines():
            line = line.strip()
            if not line:
                continue
            procs, action, rps  = line.split()
            if procs not in data:
                data[procs] = {}
                data[procs][action] = 0
            data[procs][action] = float(rps)
    return data


def plot_data(data):

    N = 6

    ind = np.arange(N)  # the x locations for the groups
    width = 0.20       # the width of the bars

    fig, ax = plt.subplots()
    vals = [data['1'][action] for action in graphs]
    rects1 = ax.bar(ind, vals, width)

    vals = [data['2'][action] for action in graphs]
    rects2 = ax.bar(ind + width, vals, width)

    vals = [data['3'][action] for action in graphs]
    rects3 = ax.bar(ind + (2 * width), vals, width)

    vals = [data['4'][action] for action in graphs]
    rects4 = ax.bar(ind + (3 * width), vals, width)

    # add some text for labels, title and axes ticks
    ax.set_ylabel('Requests per second')
    ax.set_title('How multiprocessing affects Blobs Server')
    ax.set_xticks(ind + (1.5 * width))
    ax.set_xticklabels(tuple(graphs))

    ax.legend(
        (rects1[0], rects2[0], rects3[0], rects4[0]),
        ('1 process', '2 processes', '3 processes', '4 processes'))
    ax.grid(True)

    plt.savefig('blobs-in-parallel.png')
    plt.show()


if __name__ == '__main__':
    data = get_data()
    plot_data(data)
