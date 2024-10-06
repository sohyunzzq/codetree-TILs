import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
area = []
for i in range(n):
    area.append([0] * m)

letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def in_range(x, y):
    if 0 <= x < n and 0 <= y < m:
        return True
    return False

def can_go(x, y):
    if in_range(x, y) and area[x][y] == 0:
        return True
    return False

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
x, y = 0, 0
dr = 0

area[x][y] = "A"

for i in range(1, n * m):
    nx, ny = x + dx[dr], y + dy[dr]

    if not can_go(nx, ny):
        dr = (dr + 1) % 4

        nx, ny = x + dx[dr], y + dy[dr]
    
    x, y = nx, ny
    area[x][y] = letter[i % len(letter)]

for row in area:
    for col in row:
        print(col, end = " ")
    print()