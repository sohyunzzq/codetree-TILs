n = int(input())
area = []
for i in range(n):
    area.append(list(map(int, input().split())))
visited = []
for i in range(n):
    visited.append([0] * n)

village = 0
people = []

def in_range(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False

def can_go(x, y):
    if in_range(x, y) and area[x][y] == 1 and not visited[x][y]:
        return True
    return False

def dfs(x, y):
    global num
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if can_go(nx, ny):
            visited[nx][ny] = 1
            num += 1
            dfs(nx, ny)

num = 0
for row in range(n):
    for col in range(n):
        if area[row][col] == 1 and not visited[row][col]:
            village += 1
            num = 1
            visited[row][col] = 1
            dfs(row, col)
            people.append(num)

print(village)
people.sort()
for item in people:
    print(item)