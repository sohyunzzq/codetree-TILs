def in_range(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False

def dice(dr, up, front, right):
    if dr == 0: #위
        up, front, right = front, 7 - up, right
    elif dr == 1: #오른쪽
        up, front, right = 7 - right, front, up
    elif dr == 2: #아래
        up, front, right = 7 - front, up, right
    else: #왼쪽
        up, front, right = right, front, 7 - up

    return up, front, right

dict1 = {"U": 0, "R": 1, "D": 2, "L": 3}
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

n, m, row, col = map(int, input().split())
cmd = list(input().split())
grid = []
for i in range(n):
    grid.append([0] * n)

up = 1
front = 2
right = 3
x, y = row-1, col-1

grid[x][y] = 7 - up

for i in range(m):
    dr = dict1[cmd[i]]

    if not in_range(x + dx[dr], y + dy[dr]):
        continue
    
    x += dx[dr]
    y += dy[dr]

    up, front, right = dice(dr, up, front, right)
    grid[x][y] = 7 - up

ans = 0
for i in range(n):
    ans += sum(grid[i])
print(ans)