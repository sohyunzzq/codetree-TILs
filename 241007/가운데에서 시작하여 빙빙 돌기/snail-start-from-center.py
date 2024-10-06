import sys

n = int(sys.stdin.readline().rstrip())
area = []
for i in range(n):
    area.append([0] * n)

def in_range(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False

def can_go(x, y):
    if in_range(x, y) and area[x][y] == 0:
        return True
    return False

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
x, y = n // 2, n // 2
dr = 1

area[x][y] = 1

#일단 꺾고, 그 칸을 미리 보고 갈 수 있으면 꺾는 거 확정, 0이 아니면 원래 방향 유지
for num in range(2, n * n + 1):
    ndr = (dr - 1 + 4) % 4
    nx, ny = x + dx[ndr], y + dy[ndr]

    if can_go(nx, ny):
        dr = ndr
    
    x, y = x + dx[dr], y + dy[dr]

    area[x][y] = num

for row in area:
    for col in row:
        print(col, end = " ")
    print()