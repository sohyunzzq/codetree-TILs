class Player:
    def __init__(self, x, y, dr):
        self.x = x
        self.y = y
        self.dr = dr
        self.caught = False

def in_range(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False

def get_dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def MOVE_PLAYER(player):
    #술래와의 거리가 3 이하여야 움직일 수 있음
    dist = get_dist(player.x, player.y, snailpos[0], snailpos[1])
    if dist > 3:
        return

    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    x, y = player.x, player.y
    dr = player.dr

    #지금 앞으로 갔을 때 격자에 나감?
    nx, ny = x + dx[dr], y + dy[dr]
    if not in_range(nx, ny):
        #방향을 바꿔줌
        player.dr = (dr + 2) % 4
        dr = player.dr

        #그 다음 앞에 술래가 없으면 가고 있으면 가만히
        nx, ny = x + dx[dr], y + dy[dr]
        if nx == snailpos[0] and ny == snailpos[1]:
            return
        player.x, player.y = nx, ny
    #격자 안 나감
    else:
        if nx == snailpos[0] and ny == snailpos[1]:
            return
        player.x, player.y = nx, ny

def MOVE_SNAIL():
    global mode
    global snailpos
    global snaildr
    global snail

    x, y = snailpos[0], snailpos[1]
    dr = snaildr

    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    #현재 모드가 바깥으로 가는 거면
    if mode == "OUT":
        nx, ny = x + dx[dr], y + dy[dr]

        #[0, 0] 도착
        if nx == 0 and ny == 0:
            snailpos[0], snailpos[1] = 0, 0
            mode = "IN"

            #술래 방향 바꾸고, 배열도 초기화
            snaildr = 2
            snail = []
            for i in range(n):
                snail.append([0] * n)
            snail[0][0] = 1
            return

        #격자 벗어났으면 돌려
        if not in_range(nx, ny):
            dr = (dr + 1) % 4
            snaildr = dr

            nx, ny = x + dx[dr], y + dy[dr]

        #일단 앞으로 가기
        x, y = nx, ny

        #방향을 돌릴지 말지 결정. 돌려서 다음 칸 보고 0이면 돌리고 1이면 가만히
        ndr = (snaildr + 1) % 4
        if snail[x + dx[ndr]][y + dy[ndr]] == 0:
            snaildr = ndr

    #현재 모드가 안으로 가는 거면
    else:
        nx, ny = x + dx[dr], y + dy[dr]

        #[n//2, n//2]에 도착
        if nx == n // 2 and ny == n // 2:
            mode = "OUT"

            snailpos[0], snailpos[1] = n // 2, n // 2
            #술래 방향 바꾸고, 배열도 초기화
            snaildr = 0
            snail = []
            for i in range(n):
                snail.append([0] * n)
            snail[n // 2][n // 2] = 1
            return

        #격자 벗어나거나 이미 간 곳이면 돌려
        if not in_range(nx, ny) or snail[nx][ny] != 0:
            dr = (dr - 1 + 4) % 4
            snail = dr

            nx, ny = x + dx[dr], y + dy[dr]

        #일단 앞으로 가기
        x, y = nx, ny

        #방향을 돌릴지 말지 결정. 만약 한 칸 더 갔을 때 격자 밖이거나 0이 아니면 돌려
        if not in_range(x + dx[dr], y + dy[dr]) or snail[x + dx[dr]][y + dy[dr]] != 0:
            snaildr = (snaildr - 1 + 4) % 4

    snail[x][y] = 1
    snailpos[0], snailpos[1] = x, y

def CATCH():
    global score

    cnt = 0
    #현재 칸 포함 술래 방향 3칸 볼 거임
    #만약 그 위치에 나무 있으면 걍 넘겨
    #잡을 때마다 cnt 증가시키고 점수 올려
    dr = snaildr
    x, y = snailpos[0], snailpos[1]

    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

    for i in range(3):
        nx, ny = x + dx[dr] * i, y + dy[dr] * i

        if not in_range(nx, ny) or tree[nx][ny] == 1:
            continue

        for player in players:
            if not player.caught and player.x == nx and player.y == ny:
                cnt += 1
                player.caught = True

    score += turn * cnt

n, m, h, k = map(int, input().split())
players = []
for i in range(m):
    x, y, d = map(int, input().split())
    player = Player(x-1, y-1, d)
    players.append(player)
tree = []
for i in range(n):
    tree.append([0] * n)
for i in range(h):
    x, y = map(int, input().split())
    tree[x-1][y-1] = 1

#술래 정보
snailpos = [n//2, n//2]
snaildr = 0
snail = []
for i in range(n):
    snail.append([0] * n)
snail[n//2][n//2] = 1
mode = "OUT"

score = 0
for turn in range(1, k + 1):
    #플레이어가 안 잡혔다면 순서대로 이동
    for player in players:
        if not player.caught:
            MOVE_PLAYER(player)

    #술래 이동
    MOVE_SNAIL()

    #내 시야에 걸리냐
    CATCH()

print(score)