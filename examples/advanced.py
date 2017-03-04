from __future__ import print_function

from xl import *


if __name__ == '__main__':
    # ----------------------------------------------------------------------
    sheet = 'Animal Data'
    print(SUMIFS(
        Range(Cell('h', sheet=sheet), Cell('h')),
        Range(Cell('f', sheet=sheet), Cell('f')), StrVal('Dog'),
        Range(Cell('i', sheet=sheet), Cell('i')), StrVal('Lab'),
    ))
    # ----------------------------------------------------------------------

    sheet = 'Animal Data'
    formula = SUMIFS(
        Range(Cell('c', sheet=sheet), Cell('c')),
        Range(Cell('g', sheet=sheet), Cell('g')), StrVal("<>") + StrVal('Cat'),
        Range(Cell('m', sheet=sheet), Cell('m')), StrVal('Original'),  # ==
        Range(Cell('d', sheet=sheet), Cell('d')), StrVal(">=") + DATE(
            YEAR(Cell('b', 22)),
            MONTH(Cell('b', 22)),
            DAY(Cell('b', 22))
        ),
        Range(Cell('d', sheet=sheet), Cell('d')), StrVal("<=") + DATE(
            YEAR(Cell('b', 23)),
            MONTH(Cell('b', 23)),
            DAY(Cell('b', 23))
        ),
    )
    print(formula)
    # ----------------------------------------------------------------------
