import math

from pi_digits import pi_number
from e_digits import e_number
from sequence_view import sequence_view

# https://cduck.github.io/drawsvg/


def diff():
    diff_str = ''
    for i in range(min(len(pi_number), len(e_number))):
        diff_str = diff_str + str((int(math.fabs(int(pi_number[i]) - int(e_number[i])))))
    return diff_str


def concat_e_pi():
    concat = ''
    for i in range(min(len(pi_number), len(e_number))):
        concat = concat + pi_number[i] + e_number[i]
    return concat


if __name__ == '__main__':
    sequence_view(e_number, 'e.svg', nr_rows=30, nr_columns=30, radius=5)
    sequence_view(pi_number, 'pi.svg', nr_rows=30, nr_columns=30, radius=5)
    sequence_view(diff(), 'diff.svg', nr_rows=30, nr_columns=30, radius=5)
    sequence_view(concat_e_pi(), 'concat_e_pi.svg', nr_rows=30, nr_columns=30, radius=5)
