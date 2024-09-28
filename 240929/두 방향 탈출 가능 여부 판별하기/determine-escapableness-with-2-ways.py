n, m = map(int, input().split())
area = []
for i in range(n):
    area.append(list(map(int, input().split())))

answer = []
for i in range(n):
    answer.append([0] * m)

visited = []
for i in range(n):
    visited.append([0] * m)

x, y = 0, 0
visited[0][0] = 1


def in_range(x, y):
    if 0 <= x < n and 0 <= y < m:
        return True
    return False

def can_go(x, y):
    if in_range(x, y) and area[x][y] == 1 and not visited[x][y]:
        return True
    return False


def dfs(x, y):
    global ans

    if x == n - 1 and y == m - 1:
        ans = True
    
    dx, dy = [0, 1], [1, 0]
    for i in range(2):
        nx, ny = x + dx[i], y + dy[i]
        if can_go(nx, ny):
            visited[nx][ny] = 1
            dfs(nx, ny)
    
    return False

ans = False
dfs(0, 0)

if ans:
    print(1)
else:
    print(0)