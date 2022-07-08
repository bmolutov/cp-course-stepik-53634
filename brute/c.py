"""

Author: B. Molutov

Generating all possible permutations of numbers from 1 to n.

Input: n - integer

Output: permutations

"""


def solve(n, init, curr):
    if len(curr) == n:
        print(curr)
        return

    for i in range(len(init)):
        solve(n, init[0:i] + init[i+1:], curr + [init[i]]) 


n = int(input())
solve(n, [i for i in range(1, n + 1)], [])

