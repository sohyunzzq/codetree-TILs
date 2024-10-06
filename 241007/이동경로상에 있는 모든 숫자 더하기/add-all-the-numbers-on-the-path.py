import sys

n, t = map(int, sys.stdin.readline().rstrip().split())
cmd = sys.stdin.readline().rstrip()
area = []
for i in range(n):
    area.append(list(map(int, sys.stdin.readline().rstrip().split())))

def in_range(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
x, y = n // 2, n // 2
dr = 3

ans = area[x][y]
for letter in cmd:
    if letter == "L":
        dr = (dr - 1 + 4) % 4
    elif letter == "R":
        dr = (dr + 1) % 4
    else:
        nx, ny = x + dx[dr], y + dy[dr]

        if in_range(nx, ny):
            x, y = nx, ny
            ans += area[x][y]

print(ans)