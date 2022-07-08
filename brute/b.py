"""

Author: B. Molutov

The traveling salesman problem.
(getting smallest distance by traversing permutations, 1 to n)

n - number of destinations
mat - adjacency matrix

"""


def solve(n, pts, dist, path):
    global ans, mat

    if dist >= ans:
        return
    if len(path) == n:
        ans = min(ans, dist + mat[path[-1]][0]) 
        # print('testing: ', path, dist + mat[path[-1]][0])
        return

    for i in range(len(pts)):
        solve(n, pts[0:i] + pts[i+1:], dist + mat[path[-1]][pts[i]], path + [pts[i]])


ans = 10 ** 7

n = int(input())
mat = []
for i in range(n):
    mat.append([int(i) for i in input().split()])


solve(n, [i for i in range(1, n)], 0, [0])
print(ans)

