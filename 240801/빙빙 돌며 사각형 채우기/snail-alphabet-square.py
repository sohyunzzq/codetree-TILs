alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

n, m = map(int, input().split())

area = []
for i in range(n):
    area.append([0] * m)

x, y = 0, 0
dir_num = 0
index = 0

for i in range(n * m):
    area[x][y] = alpha[index]
    index += 1
    
    if index >= len(alpha):
        index -= len(alpha)
    
    nx, ny = x + dx[dir_num], y + dy[dir_num]

    if 0 <= nx < n and 0 <= ny < m and area[nx][ny] == 0:
        x, y = nx, ny
    else:
        dir_num = (dir_num + 1) % 4
        x += dx[dir_num]
        y += dy[dir_num]

for i in range(n):
    for j in range(m):
        print(area[i][j], end = " ")
    print()