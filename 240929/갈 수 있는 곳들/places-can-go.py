from collections import deque
import sys
sys.setrecursionlimit(10000 + 1)

n, k = map(int, input().split())
area = []
for i in range(n):
    area.append(list(map(int, input().split())))

visited = []
for i in range(n):
    visited.append([0] * n)

q = deque()
for i in range(k):
    x, y = map(int, input().split())
    q.append([x-1, y-1])
    visited[x-1][y-1] = 1

def in_range(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False

def can_go(x, y):
    if in_range(x, y) and area[x][y] == 0 and not visited[x][y]:
        return True
    return False

def bfs():
    while q:
        tmp = q.popleft()
        x, y = tmp[0], tmp[1]

        dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

        for dr in range(4):
            nx, ny = x + dx[dr], y + dy[dr]

            if can_go(nx, ny):
                visited[nx][ny] = 1
                q.append([nx, ny])
                bfs()

bfs()

ans = 0
for row in visited:
    ans += sum(row)

print(ans)