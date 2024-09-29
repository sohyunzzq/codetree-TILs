from collections import deque

n, k = map(int, input().split())
area = []
for i in range(n):
    area.append(list(map(int, input().split())))

visited = []
for i in range(n):
    visited.append([0] * n)

x, y = map(int, input().split())
x, y = x-1, y-1
num = area[x][y]
visited[x][y] = 1
q = deque()
q.append([x, y])

def in_range(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False

def can_go(x, y):
    if in_range(x, y) and area[x][y] < num and not visited[x][y]:
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
                q.append([nx, ny])
                candi.append([nx, ny])
                visited[nx][ny] = 1
                bfs()
    

def choose_candi():
    maxi = 0
    lst = []

    for coor in candi:
        x, y = coor[0], coor[1]

        if area[x][y] >= maxi:
            maxi = area[x][y]
            lst.append([x, y])
    
    lst.sort(key = lambda x: (x[0], x[1]))
    return lst[0]

candi = []
coor = [x, y]
for i in range(k):
    candi = []
    bfs()
    if len(candi) == 0:
        break
    
    coor = choose_candi()
    num = area[coor[0]][coor[1]]
    q.append(coor)
    visited = []
    for i in range(n):
        visited.append([0] * n)
    visited[coor[0]][coor[1]] = 1

print(coor[0] + 1, coor[1] + 1)