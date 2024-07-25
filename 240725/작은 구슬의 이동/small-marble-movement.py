def in_range(x, y, n):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False

dct = {"R": 0, "D": 1, "L": 3, "U": 2}
#이동 방향 바뀜 → 3 - 현재위치
dx, dy = [0, 1, -1, 0], [1, 0, 0, -1]

n, t = map(int, input().split())
r, c, d = input().split()

x, y = int(r) - 1, int(c) - 1
direction = dct[d]

for i in range(t):
    if not in_range(x + dx[direction], y + dy[direction], n):
        direction = 3 - direction
    else:
        x += dx[direction]
        y += dy[direction]

print(x + 1, y + 1)