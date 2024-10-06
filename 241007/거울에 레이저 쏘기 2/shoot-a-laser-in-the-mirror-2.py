import sys

n = int(sys.stdin.readline().rstrip())
area = []
for i in range(n):
    area.append(sys.stdin.readline().rstrip())
k = int(sys.stdin.readline().rstrip())

if 0 < k <= 1 * n:
    x = 0
    y = k - 1
    dr = 1
elif 1 * n < k <= 2 * n:
    x = k - n - 1
    y = n - 1
    dr = 2
elif 2 * n < k <= 3 * n:
    x = n - 1
    y = n * 3 - k
    dr = 3
else:
    x = n * 4 - k
    y = 0
    dr = 0

def in_range(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

cnt = 0
while True:
    if not in_range(x, y):
        break
    
    if area[x][y] == "/":
        dr = 3 - dr
    elif area[x][y] == "\\":
        if dr % 2 == 0:
            dr += 1
        else:
            dr -= 1
    
    x, y = x + dx[dr], y + dy[dr]
    cnt += 1

print(cnt)