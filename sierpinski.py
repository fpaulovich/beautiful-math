# Author: Fernando V. Paulovich -- <fpaulovich@gmail.com>
#
# Copyright 2024 Fernando V. Paulovich
# License: BSD-3-Clause

import drawsvg as draw
import random

import matplotlib as mpl
import matplotlib.pyplot as plt
from numpy import linalg
import numpy as np


def sierpinski():
    triangle = np.array([[-300, -300], [300, -300], [0, 300]])
    max_dist = max(linalg.norm(triangle[0] - triangle[1]),
                   linalg.norm(triangle[0] - triangle[2]),
                   linalg.norm(triangle[1] - triangle[2]))
    cmap = plt.get_cmap('tab10')

    point = np.array([0, 0])
    nr_points = 10000

    d = draw.Drawing(800, 800, origin='center')
    for k in range(nr_points):
        vertex = random.randint(0, 2)
        color = mpl.colors.rgb2hex(cmap(linalg.norm(point - triangle[vertex]) / max_dist))

        point = [(point[0] + triangle[vertex][0]) / 2, (point[1] + triangle[vertex][1]) / 2]
        d.append(draw.Circle(point[0], point[1], 1, fill=color, stroke='black', stroke_width=0.1))

    d.set_pixel_scale(2)  # Set number of pixels per geometry unit
    d.save_svg('sierpinski.svg')
