"""

Author: B. Molutov

Splitting a number into terms.

"""


def solve(n, pos, curr):
    if sum(curr) == n:
        print(curr)
        return

    for i in range(pos, n - sum(curr) + 1):
        solve(n, i, curr + [i]) 


n = int(input())
solve(n, 1, [])

