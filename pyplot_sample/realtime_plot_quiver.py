# -*- coding: utf-8 -*-

# matplotlibでリアルタイムプロットする例
# https://qiita.com/hausen6/items/b1b54f7325745ae43e47

import numpy as np
import matplotlib.pyplot as plt


def pause_plot():
    fig, ax = plt.subplots(1, 1)
    xs = 0
    ys = 0
    th = 0

    while True:
        th += 0.1
        front = ax.quiver(xs, ys, np.cos(th), np.sin(th), color="blue", alpha=0.5)

        plt.pause(.01)
        front.remove()

if __name__ == "__main__":
    pause_plot()