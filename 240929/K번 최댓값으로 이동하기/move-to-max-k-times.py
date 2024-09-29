from collections import deque

n, k = map(int, input().split())
area = []
for i in range(n):
    area.append(list(map(int, input().split())))

x, y = map(int, input().split())

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
                candi.append([nx, ny])
                q.append([nx, ny])
                visited[nx][ny] = 1


def choose_candi():
    maxi = 0
    tmp = []
    for coor in candi:
        x, y = coor[0], coor[1]

        maxi = max(maxi, area[x][y])
    
    for coor in candi:
        x, y = coor[0], coor[1]

        if area[x][y] == maxi:
            tmp.append([x, y])
    
    tmp.sort(key = lambda x: (x[0], x[1]))

    return tmp[0]


visited = []
q = deque()
go = deque()
go.append([x-1, y-1])

candi = []
for i in range(k):
    q.append(go[-1])
    num = area[go[-1][0]][go[-1][1]]
    
    candi = []
    visited = []
    for i in range(n):
        visited.append([0] * n)    

    visited[go[-1][0]][go[-1][1]] = 1
    bfs()

    if len(candi) == 0:
        break

    nxt = choose_candi()

    go.append(nxt)

print(go[-1][0] + 1, go[-1][1] + 1)