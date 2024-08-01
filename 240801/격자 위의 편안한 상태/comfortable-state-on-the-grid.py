def in_range(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

n, m = map(int, input().split())

area = []
for i in range(n):
    area.append([0] * n)

for i in range(m):
    r, c = map(int, input().split())
    area[r-1][c-1] = 1
    cnt = 0

    for j in range(4):
        nx = r + dx[j] - 1
        ny = c + dy[j] - 1

        if in_range(nx, ny) and area[nx][ny] == 1:
            cnt += 1
    
    if cnt == 3:
        print(1)
    else:
        print(0)