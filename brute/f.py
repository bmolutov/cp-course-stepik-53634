"""

Author: B. Molutov

Generating all valid bracket sequences consisting the following 
characters: '(', ')', '[', ']', such that '(' < ')' < '[' < ']'.

Input: n - integer

Output: sequences of length 2 * n

"""

def solve(n, curr, b1, b2, stack):
    if len(curr) == 2 * n:
        ans.append(curr) 
        return

    if b1 + b2 < 2 * n - len(curr):
        solve(n, curr + '(', b1 + 1, b2, stack + ['('])

    if b1 > 0 and stack[-1] == '(':
        solve(n, curr + ')', b1 - 1, b2, stack[:-1])    

    if b2 + b1 < 2 * n - len(curr):
        solve(n, curr + '[', b1, b2 + 1, stack + ['['])

    if b2 > 0 and stack[-1] == '[':
        solve(n, curr + ']', b1, b2 - 1, stack[:-1])


ans = []
n = int(input())

solve(n, '', 0, 0, [])
for i in range(len(ans)):
    print(ans[i], i)

print('ans', ans[8232])

