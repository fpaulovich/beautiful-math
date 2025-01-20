import math

from pi_digits import pi_digits
from e_digits import e_digits
from sqr_of_two_digits import sqr_of_two_digits
from sequence_view import sequence_view

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


if __name__ == '__main__':
    sequence_view(e_digits, 'e.svg', nr_rows=30, nr_columns=30, radius=5)
    sequence_view(pi_digits, 'pi.svg', nr_rows=30, nr_columns=30, radius=5)
    sequence_view(sqr_of_two_digits, 'sqr_of_two.svg', nr_rows=30, nr_columns=30, radius=5)
    sequence_view(diff(nr_digits=1000), 'diff.svg', nr_rows=30, nr_columns=30, radius=5)
    sequence_view(concat_e_pi(nr_digits=1000), 'concat_e_pi.svg', nr_rows=30, nr_columns=30, radius=5)
