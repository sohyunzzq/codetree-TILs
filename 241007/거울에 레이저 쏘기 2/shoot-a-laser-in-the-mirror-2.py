import sys

n = int(sys.stdin.readline().rstrip())
area = []
for i in range(n):
    area.append(sys.stdin.readline().rstrip())
k = int(sys.stdin.readline().rstrip())

def get_xydr():
    if k <= 1 * n:
        return 0, k - 1, 1
    elif k <= 2 * n:
        return k - n - 1, n - 1, 2
    elif k <= 3 * n:
        return n - 1, 3 * n - k, 3
    else:
        return 4 * n - k, 0, 0

def in_range(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

x, y, dr = get_xydr()
cnt = 0

while in_range(x, y):    
    if area[x][y] == "/":
        dr = 3 - dr
    else:
        dr = dr ^ 1
    
    x, y = x + dx[dr], y + dy[dr]
    cnt += 1

print(cnt)