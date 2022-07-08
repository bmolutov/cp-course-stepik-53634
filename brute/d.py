"""

Author: B. Molutov

Generating all valid sequences consisting of characters: '(', ')'.

Input: n - integer

Output: list of sequences

"""


def solve(n, curr, bal):
    if len(curr) == 2 * n:
        ans.append(curr)
        return

    if bal < 2 * n - len(curr):
        solve(n, curr + '(', bal + 1)

    if bal > 0:
        solve(n, curr + ')', bal - 1)


ans = []
n = int(input())
solve(n, '', 0)
print(ans)

