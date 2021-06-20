# -*- coding: utf-8 -*-

# matplotlibでリアルタイムプロットする例
# https://qiita.com/hausen6/items/b1b54f7325745ae43e47

import numpy as np
import matplotlib.pyplot as plt

def pause_plot():
    fig, ax = plt.subplots(1, 1)

    while True:
        img_array = np.random.rand(40, 40)
        image = ax.imshow(img_array)

        plt.pause(0.1)
        image.remove()

if __name__ == "__main__":
    pause_plot()