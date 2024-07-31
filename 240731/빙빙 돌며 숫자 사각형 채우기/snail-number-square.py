dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

n, m = map(int, input().split())

area = []
for i in range(n):
    area.append([0] * m)

x, y = 0, 0
dir_num = 0

for i in range(1, n * m + 1):
    area[x][y] = i

    nx = x + dx[dir_num]
    ny = y + dy[dir_num]
    
    if 0 <= nx < n and 0 <= ny < m and area[nx][ny] == 0:
        x = nx
        y = ny
    else:
        dir_num = (dir_num + 1) % 4
        x += dx[dir_num]
        y += dy[dir_num]
    
for x in range(n):
    for y in range(m):
        print(area[x][y], end = " ")
    print()