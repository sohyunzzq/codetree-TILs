from collections import deque

class Human:
    def __init__(self, num, goalx, goaly):
        self.num = num
        self.x = -1
        self.y = -1
        self.goalx = goalx
        self.goaly = goaly
        self.board = False
        self.arrived = False

def in_range(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False

def get_dist(sx, sy, ex, ey):
    global pastx
    global pasty

    visited = []
    for i in range(n):
        visited.append([0] * n)
    visited[sx][sy] = 1

    pastx = []
    for i in range(n):
        pastx.append([-1] * n)
    pasty = []
    for i in range(n):
        pasty.append([-1] * n)

    q = deque()
    q.append([sx, sy])

    dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]
    while q:
        x, y = q.popleft()

        for dr in range(4):
            nx, ny = x + dx[dr], y + dy[dr]

            if nx == ex and ny == ey:
                pastx[nx][ny] = x
                pasty[nx][ny] = y
                return

            if in_range(nx, ny) and not visited[nx][ny] and area[nx][ny] != -1:
                q.append([nx, ny])
                pastx[nx][ny] = x
                pasty[nx][ny] = y
                visited[nx][ny] = 1
    return

def ALL_ARRIVED():
    for human in humans:
        if not human.arrived:
            return False
    return True

def MOVE(human):
    global pastx
    global pasty
    #최단 거리 구해서 그거로 가기
    #pastx, pasty에 경로 표시하기
    pastx = []
    for i in range(n):
        pastx.append([-1] * n)
    pasty = []
    for i in range(n):
        pasty.append([-1] * n)

    hx, hy = human.x, human.y

    visited = []
    for i in range(n):
        visited.append([0] * n)
    visited[hx][hy] = 1

    q = deque()
    q.append([hx, hy])

    dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]
    while q:
        x, y = q.popleft()

        for dr in range(4):
            nx, ny = x + dx[dr], y + dy[dr]

            if human.goalx == nx and human.goaly == ny:
                pastx[nx][ny] = x
                pasty[nx][ny] = y
                return

            if in_range(nx, ny) and not visited[nx][ny] and area[nx][ny] != -1:
                q.append([nx, ny])
                visited[nx][ny] = 1
                pastx[nx][ny] = x
                pasty[nx][ny] = y
    return

def ONESTEP(human):
    global pastx
    global pasty

    px, py = human.goalx, human.goaly
    while True:
        if pastx[px][py] == human.x and pasty[px][py] == human.y:
            human.x = px
            human.y = py
            return

        px, py = pastx[px][py], pasty[px][py]

def BASECAMP(conv):
    global pastx
    global pasty

    #가능한 베캠 후보들 [거리, [x, y]]
    candi = []

    #편의점과 모든 베캠과의 거리를 구해야 돼
    for b in base:
        bx, by = b
        #만약에 이 베캠 이제 접근 못하면 패스
        if area[bx][by] == -1:
            continue

        #편의점과 b와 거리 구하기
        get_dist(conv.goalx, conv.goaly, bx, by)

        #도달하지 못할 수도 있음
        if pastx[bx][by] == -1 and pasty[bx][by] == -1:
            continue

        #최단 경로 구해서 이제 거리 구해야 함
        px, py = bx, by
        cnt = 1
        while True:
            if pastx[px][py] == conv.goalx and pasty[px][py] == conv.goaly:
                break

            px, py = pastx[px][py], pasty[px][py]
            cnt += 1

        candi.append([cnt, [bx, by]])

    candi.sort(key = lambda x: (x[0], x[1][0], x[1][1]))

    return candi[0][1][0], candi[0][1][1]

def UNREACHABLE(b):
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    tmp = []
    for dr in range(4):
        nx, ny = b[0] + dx[dr], b[1] + dy[dr]

        if not in_range(nx, ny):
            continue

        tmp.append(area[nx][ny])

    for item in tmp:
        if item != -1:
            return

    area[b[0]][b[1]] = -1

n, m = map(int, input().split())
area = []
for i in range(n):
    area.append(list(map(int, input().split())))
base = []
for row in range(n):
    for col in range(n):
        if area[row][col] == 1:
            base.append([row, col])
            area[row][col] = "B"
humans = []
for i in range(1, m + 1):
    x, y = map(int, input().split())
    humans.append(Human(i, x-1, y-1))
    area[x-1][y-1] = i
where = []
for i in range(n):
    where.append([0] * n)

#최단 거리 구할 때 쓸 배열
pastx = []
pasty = []

t = 0
while True:
    #모든 사람이 도착했으면 종료
    if ALL_ARRIVED():
        break

    t += 1
    #격자 안에 사람이 한 명이라도 있으면 움직이기
    for human in humans:
        if not human.arrived and human.board:
            MOVE(human)
            ONESTEP(human)

    #편의점 도착하면 멈추고 편의점 먹통 표시
    for human in humans:
        if not human.arrived and human.board:
            if human.x == human.goalx and human.y == human.goaly:
                area[human.goalx][human.goaly] = -1
                human.arrived = True

    #사방에 가로막혀 있는 베캠 걍 빼버리자
    for b in base:
        UNREACHABLE(b)

    #지금 t분이고 t <= m이면 t번 사람은 베캠에 넣기
    if t <= m:
        for human in humans:
            if human.num == t:
                #가장 가까운 베캠 위치
                bx, by = BASECAMP(human)

                #베캠 접근 불가
                area[bx][by] = -1

                #사람 격자에 투입
                human.board = True
                human.x = bx
                human.y = by
                break
print(t)