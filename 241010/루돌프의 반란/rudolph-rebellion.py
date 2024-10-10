class Santa:
    def __init__(self, num, x, y):
        self.num = num #산타 번호
        self.x = x
        self.y = y
        self.score = 0
        self.alive = True #살아 있으면 True, 탈락했으면 False
        self.resume = 0 #기절 안 했으면 0, 기절했으면 다시 정상이 되는 턴

def get_dist(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2

def in_range(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False

n, m, p, c, d = map(int, input().split())

area = []
for i in range(n):
    area.append([0] * n)

x, y = map(int, input().split())

ru_pos = [x-1, y-1] #루돌프의 위치

santas = []
for i in range(p):
    num, x, y = map(int, input().split())
    santas.append(Santa(num, x-1, y-1))

    area[x-1][y-1] = num
santas.sort(key = lambda x: x.num)

def RUDOLPH_MOVE():
    global ru_pos
    global ru_dr

    dists = []
    for santa in santas:
        if santa.alive: #살아 있으면 (기절과 상관X)
            dist = get_dist(ru_pos[0], ru_pos[1], santa.x, santa.y)
            dists.append([dist, santa])

    dists.sort(key = lambda x: (x[0], -x[1].x, -x[1].y))
    target = dists[0][1]

    #8방향 중 어디로 이동해야 타겟과 가장 가까워지는지 계산하기
    #북쪽부터 시계 방향
    dx, dy = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]
    x, y = ru_pos[0], ru_pos[1]

    mini = dists[0][0]
    xx, yy = 0, 0 #루돌프가 이동한 후 위치
    for dr in range(8):
        nx, ny = x + dx[dr], y + dy[dr]
        if not in_range(nx, ny):
            continue

        dist = get_dist(nx, ny, target.x, target.y)
        if dist < mini:
            mini = dist
            xx, yy = nx, ny
            ru_dr = dr

    #루돌프가 xx, yy로 가면 가장 가까워짐
    ru_pos = [xx, yy]

def DOMINO(start, direction): #산타가 이동한 칸에 다른 산타가 있음
    #처음 도착한 산타는 start
    #연쇄적으로 밀치기

    #그 자리에 있던 산타는 nextsanta
    for santa in santas:
        if santa.num == area[start.x][start.y]:
            nextsanta = santa
            break

    #그 자리는 start가 먹기
    area[start.x][start.y] = start.num

    #같은 방향으로 한 칸 밀려나기
    dx, dy = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]

    nextsanta.x += dx[direction]
    nextsanta.y += dy[direction]

    #격자 밖으로 나가면 탈락
    if not in_range(nextsanta.x, nextsanta.y):
        nextsanta.alive = False
        return

    #근데 그 자리에 또 누가 있다면 또 연쇄
    if area[nextsanta.x][nextsanta.y] != 0:
        DOMINO(nextsanta, direction)
    else:
        area[nextsanta.x][nextsanta.y] = nextsanta.num



def RU_2_SANTA(): #루돌프가 산타에게
    for santa in santas:
        if santa.alive and santa.x == ru_pos[0] and santa.y == ru_pos[1]:
            #산타 점수 획득
            santa.score += c

            #기존 산타 위치 지워주기
            area[santa.x][santa.y] = 0

            #산타가 루돌프 방향대로 밀려남
            #루돌프가 온 방향은 ru_dr
            dx, dy = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]
            santa.x += dx[ru_dr] * c
            santa.y += dy[ru_dr] * c

            #만약 밀려난 후 격자 밖이라면
            if not in_range(santa.x, santa.y):
                santa.alive = False
                return

            #산타 위치 업데이트
            #만약 다른 산타가 있으면 아직 업데이트 ㄴㄴ
            if area[santa.x][santa.y] != 0:
                DOMINO(santa, ru_dr)
            else:
                area[santa.x][santa.y] = santa.num

            #산타 기절
            santa.resume = t + 2
            break

def SANTA_MOVE(santa):
    global san_dr

    #네 방향 전부 체크
    #격자 밖이거나 누구 있으면 거기론 못 감
    #현재 거리를 잰 후, 가까워지지 못하면 안 움직임
    x, y = santa.x, santa.y
    now_dist = get_dist(x, y, ru_pos[0], ru_pos[1])

    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

    #가까워질 수 있는 방향 후보 [움직인 후 거리, 방향]
    candi = []
    for dr in range(4):
        nx, ny = x + dx[dr], y + dy[dr]
        if not in_range(nx, ny) or area[nx][ny] != 0:
            continue

        dist = get_dist(nx, ny, ru_pos[0], ru_pos[1])
        if dist > now_dist:
            continue

        candi.append([dist, dr])

    #후보 정렬: 거리 -> 방향
    candi.sort(key = lambda x: (x[0], x[1]))

    if len(candi) == 0:
        return

    target = candi[0]

    #기존 위치 없애주기
    area[santa.x][santa.y] = 0

    san_dr = target[1]
    santa.x += dx[san_dr]
    santa.y += dy[san_dr]
    area[santa.x][santa.y] = santa.num

def SANTA_2_RU(santa): #산타가 루돌프에게
    if santa.x == ru_pos[0] and santa.y == ru_pos[1]:
        #산타 점수 획득
        santa.score += d

        #기존 산타 위치 지워주기
        area[santa.x][santa.y] = 0

        #산타가 온 방향 반대로 d칸 밀려남
        #산타가 온 방향은 san_dr
        tmp_dr = (san_dr - 2 + 4) % 4
        dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
        santa.x += dx[tmp_dr] * d
        santa.y += dy[tmp_dr] * d

        #만약 밀려난 후 격자 밖이라면
        if not in_range(santa.x, santa.y):
            santa.alive = False
            return

        #산타 위치 업데이트
        #만약 다른 산타가 있으면 아직 업데이트 ㄴㄴ
        if area[santa.x][santa.y] != 0:
            DOMINO(santa, tmp_dr * 2)
        else:
            area[santa.x][santa.y] = santa.num

        #산타 기절
        santa.resume = t + 2

def ALL_DEAD():
    for santa in santas:
        if santa.alive:
            return False
    return True

ru_dr = 0 #북쪽부터 0, 1, ..., 7
san_dr = 0 #북쪽부터 0, 1, 2, 3
#턴 시작
for t in range(1, m + 1):
    #루돌프 이동
    RUDOLPH_MOVE()

    #부딪쳤는지 확인
    RU_2_SANTA()

    #산타 1번부터 p번까지 이동
    #살아 있는지 -> 기절했는지 확인해주기
    for santa in santas:
        if santa.alive:
            #아직 기절함
            if 0 < santa.resume < t or santa.resume > t:
                continue
            #현재 턴에서 정상화됨
            elif santa.resume == t:
                santa.resume = 0

            #산타 이동하기
            SANTA_MOVE(santa)

            #부딪쳤는지 확인
            SANTA_2_RU(santa)

    #살아 있는 산타 +1점씩
    for santa in santas:
        if santa.alive:
            santa.score += 1

    #게임 종료인지 체크
    if ALL_DEAD():
        break

for santa in santas:
    print(santa.score, end = " ")