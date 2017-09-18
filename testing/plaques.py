from __future__ import division, print_function


def calculateTiter(counts, dilutions, volume):
    """
    Calculate the titer given counts, volume, and dilution...
    """

    if volume <= 0:
        raise ValueError('Volume cannot be <= 0')

    if not counts:
        raise ValueError('You must pass at least one count')

    if len(counts) != len(dilutions):
        raise ValueError('You must pass the same number of counts '
                         'as dilutions')

    if not all(type(count) is int for count in counts):
        raise ValueError('Counts must be integers!')

    titer = 0

    for count, dilution in zip(counts, dilutions):
        titer += count * dilution

    return titer / volume
