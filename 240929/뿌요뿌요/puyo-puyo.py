n = int(input())
area = []
for i in range(n):
    area.append(list(map(int, input().split())))
visited = []
for i in range(n):
    visited.append([0] * n)


def in_range(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False

def can_go(x, y):
    if in_range(x, y) and area[x][y] == num and not visited[x][y]:
        return True
    return False

def dfs(x, y):
    global cnt
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

    for dr in range(4):
        nx, ny = x + dx[dr], y + dy[dr]

        if can_go(nx, ny):
            cnt += 1
            visited[nx][ny] = 1
            dfs(nx, ny)


blocks = []
cnt = 0
for row in range(n):
    for col in range(n):
        num = area[row][col]
        if can_go(row, col):
            cnt = 1
            visited[row][col] = 1
            dfs(row, col)
        
            blocks.append(cnt)

cnt = 0
for item in blocks:
    if item >= 4:
        cnt += 1

print(cnt, max(blocks))