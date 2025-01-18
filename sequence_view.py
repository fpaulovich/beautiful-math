import drawsvg as draw
import matplotlib as mpl
import matplotlib.pyplot as plt

# https://cduck.github.io/drawsvg/


def sequence_view(number, filename='sequence.svg', nr_rows=20, nr_columns=20, radius=5):
    cmap = plt.get_cmap('tab10')

    width = 2 * (nr_columns * (radius * 2))
    height = 2 * (nr_rows * (radius * 2))
    d = draw.Drawing(width, height, origin=(0, 0))

    # background
    d.append(draw.Rectangle(x=0,
                            y=0,
                            width=width,
                            height=height,
                            fill='#293133'))

    for i in range(nr_rows):
        for j in range(nr_columns):
            k = (i * nr_columns) + j
            digit = int(number[k])
            color = mpl.colors.rgb2hex(cmap(digit / 9.0))

            # connect horizontal
            if j < (nr_columns - 1):
                if number[k] == number[k + 1]:
                    d.append(draw.Line(sx=(2 * j * (radius * 2)) + 2*radius,
                                       sy=(2 * i * (radius * 2)) + 2*radius,
                                       #
                                       ex=(2 * (j + 1) * (radius * 2)) + 2*radius,
                                       ey=(2 * i * (radius * 2)) + 2*radius,
                                       #
                                       stroke=color,
                                       stroke_width=5.0))

            # connect vertical and diagonal
            if i < (nr_rows - 1):
                # vertical
                if number[k] == number[k + nr_columns]:
                    d.append(draw.Line(sx=(2 * j * (radius * 2)) + 2*radius,
                                       sy=(2 * i * (radius * 2)) + 2*radius,
                                       #
                                       ex=(2 * j * (radius * 2)) + 2*radius,
                                       ey=(2 * (i + 1) * (radius * 2)) + 2*radius,
                                       #
                                       stroke=color,
                                       stroke_width=5.0))

                # diagonal left
                if j > 0 and number[k] == number[k + nr_columns - 1]:
                    d.append(draw.Line(sx=(2 * j * (radius * 2)) + 2*radius,
                                       sy=(2 * i * (radius * 2)) + 2*radius,
                                       #
                                       ex=(2 * (j - 1) * (radius * 2)) + 2*radius,
                                       ey=(2 * (i + 1) * (radius * 2)) + 2*radius,
                                       #
                                       stroke=color,
                                       stroke_width=5.0))

                # diagonal right
                if j < (nr_columns - 1) and number[k] == number[k + nr_columns + 1]:
                    d.append(draw.Line(sx=(2 * j * (radius * 2)) + 2*radius,
                                       sy=(2 * i * (radius * 2)) + 2*radius,
                                       #
                                       ex=(2 * (j + 1) * (radius * 2)) + 2*radius,
                                       ey=(2 * (i + 1) * (radius * 2)) + 2*radius,
                                       #
                                       stroke=color,
                                       stroke_width=5.0))

            # draw circle
            d.append(draw.Circle(cx=(2 * j * (radius * 2)) + 2*radius,
                                 cy=(2 * i * (radius * 2)) + 2*radius,
                                 r=radius,
                                 fill=color))

    d.set_pixel_scale(2)  # Set number of pixels per geometry unit
    d.save_svg(filename)
