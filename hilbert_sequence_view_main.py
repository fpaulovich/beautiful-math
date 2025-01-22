# Author: Fernando V. Paulovich -- <fpaulovich@gmail.com>
#
# Copyright 2024 Fernando V. Paulovich
# License: BSD-3-Clause

import math

from pi_digits import pi_digits
from e_digits import e_digits
from sqr_of_two_digits import sqr_of_two_digits
from hilbert_sequence_view import hilbert_sequence_view

# https://cduck.github.io/drawsvg/


def diff(nr_digits=100):
    diff_str = ''
    for i in range(min(nr_digits, len(pi_digits), len(e_digits))):
        diff_str = diff_str + str((int(math.fabs(int(pi_digits[i]) - int(e_digits[i])))))
    return diff_str


def concat_e_pi(nr_digits=100):
    concat = ''
    for i in range(min(nr_digits, len(pi_digits), len(e_digits))):
        concat = concat + pi_digits[i] + e_digits[i]
    return concat


def convert_base_10_to_2(number, nr_digits=100):
    conversion = ''

    from_10_to_2 = {'0': '0',
                    '1': '1',
                    '2': '10',
                    '3': '11',
                    '4': '100',
                    '5': '101',
                    '6': '110',
                    '7': '111',
                    '8': '1000',
                    '9': '1001'}

    for i in range(min(nr_digits, len(pi_digits), len(e_digits))):
        conversion = conversion + from_10_to_2[number[i]]
    return conversion


def convert_base_10_to_3(number, nr_digits=100):
    conversion = ''

    from_10_to_3 = {'0': '0',
                    '1': '1',
                    '2': '2',
                    '3': '10',
                    '4': '11',
                    '5': '12',
                    '6': '20',
                    '7': '21',
                    '8': '22',
                    '9': '100'}

    for i in range(min(nr_digits, len(pi_digits), len(e_digits))):
        conversion = conversion + from_10_to_3[number[i]]
    return conversion


def convert_base_10_to_4(number, nr_digits=100):
    conversion = ''

    from_10_to_4 = {'0': '0',
                    '1': '1',
                    '2': '2',
                    '3': '3',
                    '4': '10',
                    '5': '11',
                    '6': '12',
                    '7': '13',
                    '8': '20',
                    '9': '21'}

    for i in range(min(nr_digits, len(pi_digits), len(e_digits))):
        conversion = conversion + from_10_to_4[number[i]]
    return conversion


if __name__ == '__main__':
    size = 1024  # always power of 2

    hilbert_sequence_view(pi_digits, 'pi_hilbert.svg', size=size, radius=5)
    hilbert_sequence_view(e_digits, 'e_hilbert.svg', size=size, radius=5)
    hilbert_sequence_view(sqr_of_two_digits, 'sqr_of_two_digits_hilbert.svg', size=size, radius=5)
    hilbert_sequence_view(diff(nr_digits=size), 'diff_pi_e_hilbert.svg', size=size, radius=5)
    hilbert_sequence_view(concat_e_pi(nr_digits=size), 'concat_pi_e_hilbert.svg', size=size, radius=5)
    hilbert_sequence_view(convert_base_10_to_4(pi_digits, nr_digits=size), 'pi_base_4_hilbert.svg', size=size, radius=5)