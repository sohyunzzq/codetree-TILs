from collections import deque

def laser_possible():
    global pastx
    global pasty

    q = deque()
    q.append([attacker[0], attacker[1]])

    pastx = []
    for i in range(n):
        pastx.append([-1] * m)

    pasty = []
    for i in range(n):
        pasty.append([-1] * m)

    visited = []
    for i in range(n):
        visited.append([0] * m)

    visited[attacker[0]][attacker[1]] = 1

    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    while q:
        x, y = q.popleft()
        visited[x][y] = 1

        #피해자에 도달했으면 멈추기
        if x == victim[0] and y == victim[1]:
            return True

        for dr in range(4):
            nx, ny = (x + dx[dr]) % n, (y + dy[dr]) % m

            if power[nx][ny] != 0 and not visited[nx][ny]:
                q.append([nx, ny])
                pastx[nx][ny] = x
                pasty[nx][ny] = y
                visited[nx][ny] = 1

    #갈 수 있는 데 다 갔는데 도달 못함
    return False

def ONLY_ONE():
    cnt = 0
    for row in range(n):
        for col in range(m):
            if power[row][col] > 0:
                cnt += 1

                if cnt > 1:
                    return False
    return True

def FIND_ATTACKER():
    weak = []
    mini = 5000

    #가장 낮은 공격력을 mini에 담기
    for row in range(n):
        for col in range(m):
            #공격력이 0이면 부서진 거라 무시
            if power[row][col] <= 0:
                continue

            mini = min(mini, power[row][col])

    #가장 약한 애 찾기 [row, col, 최근에 공격한 거]
    for row in range(n):
        for col in range(m):
            if power[row][col] == mini:
                weak.append([row, col, recent[row][col]])

    #후보가 하나면 바로 리턴
    if len(weak) == 1:
        return [weak[0][0], weak[0][1]]

    #여러 개면 정렬: 가장 최근(내림차), r + c(내림차), c(내림차)
    weak.sort(key = lambda x: (-x[2], -(x[0] + x[1]), -x[1]))
    return [weak[0][0], weak[0][1]]

def FIND_VICTIM():
    strong = []
    maxi = 0

    #피해자는 내가 아니어야 됨

    #가장 높은 공격력을 maxi에 담기
    for row in range(n):
        for col in range(m):
            if row == attacker[0] and col == attacker[1]:
                continue
            maxi = max(maxi, power[row][col])

    #가장 센 애 찾기 [row, col, 최근에 공격한 거]
    for row in range(n):
        for col in range(m):
            if power[row][col] == maxi:
                if row == attacker[0] and col == attacker[1]:
                    continue
                strong.append([row, col, recent[row][col]])

    #후보가 하나면 바로 리턴
    if len(strong) == 1:
        return [strong[0][0], strong[0][1]]

    #여러 개면 정렬: 가장 옛날(오름차), r + c(오름차), c(오름차)
    strong.sort(key = lambda x: (x[2], x[0] + x[1], x[1]))
    return [strong[0][0], strong[0][1]]

def BOMB(attacker, victim):
    dx, dy = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]
    x, y = victim[0], victim[1]

    power[x][y] -= power[attacker[0]][attacker[1]]
    if power[x][y] < 0:
        power[x][y] = 0
    attacked_now[x][y] = True

    for dr in range(8):
        nx, ny = (x + dx[dr]) % n, (y + dy[dr]) % m

        if nx == attacker[0] and ny == attacker[1]:
            continue

        power[nx][ny] -= power[attacker[0]][attacker[1]] // 2
        if power[nx][ny] < 0:
            power[nx][ny] = 0
        attacked_now[nx][ny] = True

def ATTACK(attacker, victim):
    if laser_possible():
        #레이저 공격 가능함
        #역추적하면서 공격하기

        #일단 피해자 먼저
        power[victim[0]][victim[1]] -= power[attacker[0]][attacker[1]]
        if power[victim[0]][victim[1]] < 0:
            power[victim[0]][victim[1]] = 0
        attacked_now[victim[0]][victim[1]] = True

        #피해자 오기 직전 칸
        px, py = pastx[victim[0]][victim[1]], pasty[victim[0]][victim[1]]
        while True:
            if px == attacker[0] and py == attacker[1]:
                return

            power[px][py] -= power[attacker[0]][attacker[1]] // 2
            if power[px][py] < 0:
                power[px][py] = 0
            attacked_now[px][py] = True

            nx, ny = pastx[px][py], pasty[px][py]
            px, py = nx, ny

    else:
        BOMB(attacker, victim)

def POWERUP():
    for row in range(n):
        for col in range(m):
            if row == attacker[0] and col == attacker[1]:
                continue

            if not attacked_now[row][col] and power[row][col] > 0:
                power[row][col] += 1
                attacked_now[row][col] = False

def GET_MAX_POWER():
    maxi = 0
    for row in range(n):
        for col in range(m):
            maxi = max(maxi, power[row][col])

    return maxi

n, m, k = map(int, input().split())

#공격력을 저장할 배열
power = []
for i in range(n):
    power.append(list(map(int, input().split())))

#언제 최근에 공격했는지
recent = []
for i in range(n):
    recent.append([0] * m)

#방금 다쳤는지
attacked_now = []

#경로 저장하는 배열들
pastx = []
pasty = []

for turn in range(1, k + 1):
    #안 부서진 포탑이 하나밖에 없으면 즉시 종료
    if ONLY_ONE():
        break

    #이번 턴에 다쳤는지
    attacked_now = []
    for i in range(n):
        attacked_now.append([False] * m)

    #공격자 찾기, 공격력 증가
    attacker = FIND_ATTACKER()
    power[attacker[0]][attacker[1]] += n + m

    #피해자 찾기
    victim = FIND_VICTIM()

    #공격
    ATTACK(attacker, victim)
    recent[attacker[0]][attacker[1]] = turn

    #안 다친 애들 공격력 1씩 증가
    POWERUP()

maxi = GET_MAX_POWER()

print(maxi)