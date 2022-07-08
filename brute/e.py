"""

Author: B. Molutov

Given a list consisting of characters: '(', ')', '[', ']'.
Check their validity.

Input: list of strings

Output: values of validity

"""


def solve(seq):
    st = []
    for c in seq:
        if len(st) == 0:
            st.append(c)
            continue
        if c == '(' or c == '[':
            st.append(c)
        elif c == ')' and st[-1] == '(':
            st.pop(-1)
        elif c == ']' and st[-1] == '[':
            st.pop(-1)
        else:
            return False
    return True 


lst = [i for i in input().split()]

for i in lst:
    print(solve(i))

