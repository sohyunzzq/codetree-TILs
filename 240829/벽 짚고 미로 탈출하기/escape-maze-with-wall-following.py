def in_range(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False

def is_wall(x, y):
    if grid[x][y] == "#":
        return True
    return False

def rotate(dr, x, y):
    for _ in range(2):
        dr = (dr - 1 + 4) % 4 #CCW
        if not is_wall(x + dx[dr], y + dy[dr]):
            return dr
    return -1


dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
dr = 1

n = int(input())
x, y = map(int, input().split())
grid = []
for i in range(n):
    grid.append([0] * n)
for i in range(n):
    tmp = input()
    for j in range(n):
        grid[i][j] = tmp[j]

x -= 1
y -= 1
startx, starty = x, y

#격자 벗어나면 성공
#오른쪽이 벽이 아니면 CW 회전
#오른쪽에 벽이 있고, 앞에 벽이 없으면 가기
#                        벽이 있으면 앞에 벽이 없을 때까지 CCW 회전

t = 0
while True:
    right = (dr + 1) % 4 #현재 방향의 오른쪽

    if in_range(x, y) and not is_wall(x + dx[right], y + dy[right]): #오른쪽이 벽이 아님
        dr = right

    if not is_wall(x + dx[dr], y + dy[dr]): #앞에 벽이 없음
        x += dx[dr]
        y += dy[dr]
        t += 1
    else: #앞에 벽이 있음
        dr = rotate(dr, x, y)
        if dr == -1:
            t = -1
            break
        continue

    if not in_range(x, y): #성공
        break

    if x == startx and y == starty:
        t = -1
        break

print(t)