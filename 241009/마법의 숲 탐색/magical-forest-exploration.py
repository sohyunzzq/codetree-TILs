from collections import deque

n, m, k = map(int, input().split())
area = []
for i in range(n):
    area.append([0] * m)

def in_range_or_zero(x, y):
    if x < n and 0 <= y < m:
        return True
    return False

def in_range(x, y):
    if 0 <= x < n and 0 <= y < m:
        return True
    return False

def can_go(x, y): #x, y는 요정의 위치고, 골렘이 겹치는지 봐야 함
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

    for dr in range(4):
        nx, ny = x + dx[dr], y + dy[dr]

        #맨 처음에 내려올 때는 0보다 작아도 통과시켜줘야 함
        if nx < 0:
            if 0 <= y < m:
                continue
            else:
                return False

        if not in_range_or_zero(nx, ny) or area[nx][ny] != 0:
            return False

    return True

def OUTSIDE(x, y):
    if not in_range(x, y):
        return True

    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    for dr in range(4):
        nx, ny = x + dx[dr], y + dy[dr]

        if not in_range(nx, ny):
            return True

    return False

def DRAW_MINE(x, y):
    area[x][y] = "NB"
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    for dr in range(4):
        area[x + dx[dr]][y + dy[dr]] = "NB"

    area[x + dx[ex]][y + dy[ex]] = "NE"

def DRAW(x, y):
    area[x][y] = "EB"
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    for dr in range(4):
        area[x + dx[dr]][y + dy[dr]] = "EB"

    area[x + dx[ex]][y + dy[ex]] = "BE"

def NB(x, y):
    global visited
    if in_range(x, y) and not visited[x][y] and (area[x][y] == "NB" or area[x][y] == "NE"):
        return True
    return False

def E(x, y):
    global visited
    if in_range(x, y) and not visited[x][y] and area[x][y] != 0:
        return True
    return False

def EB(x, y):
    global visited
    if in_range(x, y) and not visited[x][y] and (area[x][y] == "EB" or area[x][y] == "EE"):
        return True
    return False

def GET_SCORE_BFS():
    global q
    global visited

    maxi = 0
    while q:
        x, y = q.popleft()
        state = area[x][y]

        dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

        for dr in range(4):
            nx, ny = x + dx[dr], y + dy[dr]

            if (state == "NB" and NB(nx, ny)) or \
                    ((state == "NE" or state == "EE") and E(nx, ny)) or \
                    (state == "EB" and EB(nx, ny)):
                visited[nx][ny] = 1
                maxi = max(maxi, nx + 1)
                q.append([nx, ny])

    return maxi

q = deque()
visited = []
def score(x, y):
    global ans
    global q
    global visited

    q = deque()
    q.append([x, y])

    visited = []
    for i in range(n):
        visited.append([0] * m)

    visited[x][y] = 1

    ans += GET_SCORE_BFS()

ans = 0
for _ in range(k):
    c, ex = map(int, input().split())

    fairy = [-2, c-1]

    while True:
        nx, ny = fairy[0] + 1, fairy[1] #바로 아래로 가기
        if can_go(nx, ny):
            fairy[0] = nx
            fairy[1] = ny
            continue

        nx, ny = fairy[0], fairy[1] - 1 #서쪽으로 한 칸 이동
        if can_go(nx, ny):
            nx, ny = nx + 1, ny #바로 아래로
            if can_go(nx, ny):
                fairy[0] = nx
                fairy[1] = ny
                ex = (ex - 1 + 4) % 4
                continue

        nx, ny = fairy[0], fairy[1] + 1 #동쪽으로 한 칸 이동
        if can_go(nx, ny):
            nx, ny = nx + 1, ny #바로 아래로
            if can_go(nx, ny):
                fairy[0] = nx
                fairy[1] = ny
                ex = (ex + 1) % 4
                continue

        break #더 이상 못 내려가면 나오기

    #만약 골렘이 넘치면 배열 초기화
    if OUTSIDE(fairy[0], fairy[1]):
        area = []
        for i in range(n):
            area.append([0] * m)

        continue

    #안 넘치면 골렘 위치 표시하기
    DRAW_MINE(fairy[0], fairy[1])

    #점수 계산하기
    score(fairy[0], fairy[1])

    #내 거 기존 거랑 똑같이 표시해주기
    DRAW(fairy[0], fairy[1])

print(ans)