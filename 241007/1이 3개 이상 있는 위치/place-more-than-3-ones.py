import sys

n = int(sys.stdin.readline())
area = []
for i in range(n):
    area.append(list(map(int, sys.stdin.readline().rstrip().split())))

def in_range(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False

ans = 0
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
for row in range(n):
    for col in range(n):
        cnt = 0

        for dr in range(4):
            nx, ny = row + dx[dr], col + dy[dr]

            if not in_range(nx, ny):
                continue
            
            if area[nx][ny] == 1:
                cnt += 1
    
        if cnt >= 3:
            ans += 1

print(ans)