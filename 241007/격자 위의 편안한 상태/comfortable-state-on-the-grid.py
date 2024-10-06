import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
area = []
for i in range(n):
    area.append([0] * n)

def in_range(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
for i in range(m):
    r, c = map(int, sys.stdin.readline().rstrip().split())
    area[r-1][c-1] = 1 #색칠

    cnt = 0
    for dr in range(4):
        nx, ny = int(r) - 1 + dx[dr], int(c) - 1 + dy[dr]

        if in_range(nx, ny) and area[nx][ny] == 1:
            cnt += 1

    if cnt >= 3:
        print(1)
    else:
        print(0)