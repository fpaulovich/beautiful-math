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


if __name__ == '__main__':
    hilbert_sequence_view(pi_digits, 'pi_hilbert.svg', size=1024, radius=5)
    hilbert_sequence_view(e_digits, 'e_hilbert.svg', size=1024, radius=5)
    hilbert_sequence_view(sqr_of_two_digits, 'sqr_of_two_digits_hilbert.svg', size=1024, radius=5)
    hilbert_sequence_view(diff(nr_digits=1024), 'diff_hilbert.svg', size=1024, radius=5)
    hilbert_sequence_view(concat_e_pi(nr_digits=1024), 'concat_e_pi_hilbert.svg', size=1024, radius=5)
