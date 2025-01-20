import drawsvg as draw
import matplotlib as mpl
import matplotlib.pyplot as plt

# https://cduck.github.io/drawsvg/

# hilbert encode was based on
# https://github.com/saehm/hagrid/blob/master/src/hilbert.js


def rotate(size, px, py, rx, ry):
    if ry == 0:
        if rx == 1:
            px = size - 1 - px
            py = size - 1 - py
        return [py, px]
    return [px, py]


def hilbert_decode(n, size):
    t = n
    [px, py] = [0, 0]
    s = 1
    while s < size:
        rx = 1 & int(t / 2)
        ry = 1 & (t ^ rx)
        [px, py] = rotate(s, px, py, rx, ry)
        px += (s * rx)
        py += (s * ry)
        t = t >> 2
        s *= 2
    return [px, py]


def hilbert_sequence_view(number, filename='sequence-hilbert.svg', size=1024, radius=5):
    cmap = plt.get_cmap('tab10')

    nr_columns = 0
    nr_rows = 0

    for i in range(size):
        index = hilbert_decode(i, size)
        nr_rows = max(nr_rows, index[0])
        nr_columns = max(nr_columns, index[1])
    nr_rows = nr_rows + 1
    nr_columns = nr_columns + 1

    width = 2 * (nr_columns * (radius * 2))
    height = 2 * (nr_rows * (radius * 2))
    d = draw.Drawing(width, height, origin=(0, 0))

    # background
    d.append(draw.Rectangle(x=0,
                            y=0,
                            width=width,
                            height=height,
                            fill='#3D3F41'))

    for k in range(size):
        index = hilbert_decode(k, size)
        digit = int(number[k])
        color = mpl.colors.rgb2hex(cmap(digit / 9.0))

        # draw circle
        d.append(draw.Circle(cx=(2 * index[1] * (radius * 2)) + 2 * radius,
                             cy=(2 * index[0] * (radius * 2)) + 2 * radius,
                             r=radius,
                             fill=color))

        # connect to next
        if k < (size - 1):
            if number[k] == number[k + 1]:
                index_next = hilbert_decode(k + 1, size)
                d.append(draw.Line(sx=(2 * index[1] * (radius * 2)) + 2 * radius,
                                   sy=(2 * index[0] * (radius * 2)) + 2 * radius,
                                   #
                                   ex=(2 * index_next[1] * (radius * 2)) + 2 * radius,
                                   ey=(2 * index_next[0] * (radius * 2)) + 2 * radius,
                                   #
                                   stroke=color,
                                   stroke_width=5.0))

        # if k < (size - 2):
        #     if number[k] == number[k + 2]:
        #         index_next = hilbert_decode(k + 2, size)
        #         d.append(draw.Line(sx=(2 * index[1] * (radius * 2)) + 2 * radius,
        #                            sy=(2 * index[0] * (radius * 2)) + 2 * radius,
        #                            #
        #                            ex=(2 * index_next[1] * (radius * 2)) + 2 * radius,
        #                            ey=(2 * index_next[0] * (radius * 2)) + 2 * radius,
        #                            #
        #                            stroke=color,
        #                            stroke_width=5.0))

    d.set_pixel_scale(2)  # Set number of pixels per geometry unit
    d.save_svg(filename)

