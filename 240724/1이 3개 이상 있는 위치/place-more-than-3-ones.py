def in_range(x, y, n):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

n = int(input())

area = []
for i in range(n):
    area.append(list(map(int, input().split())))

res = 0
for x in range(n):
    for y in range(n):
        cnt = 0
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny, n) and area[nx][ny] == 1:
                cnt += 1
        if cnt >= 3:
            res += 1

print(res)