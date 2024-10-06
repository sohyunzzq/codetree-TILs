import sys

n, t = map(int, sys.stdin.readline().rstrip().split())
r, c, d = sys.stdin.readline().rstrip().split()

def in_range(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False

dict1 = {"R": 0, "D": 1, "L": 2, "U": 3}
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

x, y = int(r)-1, int(c)-1
dr = dict1[d]

for i in range(t):
    nx, ny = x + dx[dr], y + dy[dr]

    if not in_range(nx, ny):
        dr = (dr - 2 + 4) % 4
        continue
    
    x, y = nx, ny

print(x+1, y+1)