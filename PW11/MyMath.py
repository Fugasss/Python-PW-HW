# repeats number 'n' from lower bound 'lbound' to upper bound 'ubound'
# n -> [lbound; ubound)
#
# examples:
# repeat(32, 1, 15) returns 4
# repeat(32, 0, 15) return 2
# repeat(30, 3, 10) return 9
def repeat(n: int, lbound: int, ubound: int):
    return n - n // ubound * (ubound - lbound)
