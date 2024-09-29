from collections import deque

n, m = map(int, input().split())
area = []
for i in range(n):
    area.append(list(map(int, input().split())))
visited = []
for i in range(n):
    visited.append([0] * m)

def in_range(x, y):
    if 0 <= x < n and 0 <= y < m:
        return True
    return False

def can_go(x, y):
    if in_range(x, y) and area[x][y] == 1 and not visited[x][y]:
        return True
    return False

q = deque()
q.append([0, 0])

ans = 0
def bfs():
    global ans
    while q:
        tmp = q.popleft()
        x, y = tmp[0], tmp[1]

        if x == n - 1 and y == m - 1:
            ans = 1

        dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

        for dr in range(4):
            nx, ny = x + dx[dr], y + dy[dr]

            if can_go(nx, ny):
                visited[nx][ny] = 1
                q.append([nx, ny])

visited[0][0] = 1
bfs()
print(ans)