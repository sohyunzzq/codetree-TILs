dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]

n = int(input())

area = []
for i in range(n):
    area.append([0] * n)

x, y = n // 2, n // 2
dir_num = 3

for i in range(1, n * n + 1):
    area[x][y] = i

    if x >= n or y >= n or n == 1:
        break
    ndir_num = (dir_num + 1) % 4
    nx = x + dx[ndir_num]
    ny = y + dy[ndir_num]

    if area[nx][ny] == 0:
        x, y = nx, ny
        dir_num = ndir_num
    else:
        x += dx[dir_num]
        y += dy[dir_num]

for i in range(n):
    for j in range(n):
        print(area[i][j], end = " ")
    print()