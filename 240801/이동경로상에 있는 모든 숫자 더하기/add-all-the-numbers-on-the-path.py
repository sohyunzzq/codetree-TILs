def in_range(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

n, t = map(int, input().split())

area = []
for i in range(n):
    area.append([0] * n)

index = 1
for i in range(n):
    for j in range(n):
        area[i][j] = index
        index += 1

cmd = input()

x, y = n // 2, n // 2
result = area[x][y]
dir_num = 0

for i in range(t):
    if cmd[i] == "F":
        nx, ny = x + dx[dir_num], y + dy[dir_num]
        if in_range(nx, ny):
            x += dx[dir_num]
            y += dy[dir_num]
            result += area[x][y]
    elif cmd[i] == "L":
        dir_num = (dir_num - 1 + 4) % 4
    else:
        dir_num = (dir_num + 1) % 4

print(result)