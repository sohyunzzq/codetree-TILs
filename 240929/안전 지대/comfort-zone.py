#k를 초과하면 뭉텅이 취급
#뭉텅이의 개수가 최대인 경우를 찾아라
#최대일 때 뭉텅이 개수, 그때의 K (여러 개면 최솟값)

n, m = map(int, input().split())
area = []
for i in range(n):
    area.append(list(map(int, input().split())))

max_k = 0
for row in area:
    for col in row:
        max_k = max(max_k, col)
min_k = max_k
for row in area:
    for col in row:
        min_k = min(min_k, col)

def in_range(x, y):
    if 0 <= x < n and 0 <= y < m:
        return True
    return False

def can_go(x, y):
    if in_range(x, y) and area[x][y] > k and not visited[x][y]:
        return True
    return False

def dfs(x, y):
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

    for dr in range(4):
        nx, ny = x + dx[dr], y + dy[dr]

        if can_go(nx, ny):
            visited[nx][ny] = 1
            dfs(nx, ny)
    
klst = []
for k in range(min_k, max_k + 1):
    visited = []
    for i in range(n):
        visited.append([0] * m)

    comfort = 0
    for row in range(n):
        for col in range(m):
            if can_go(row, col):
                visited[row][col] = 1
                comfort += 1
                dfs(row, col)
    
    klst.append([k, comfort])

klst.sort(key = lambda x: (-x[1], x[0]))
print(klst[0][0], klst[0][1])