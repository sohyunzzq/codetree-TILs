class Player:
    def __init__(self, num, x, y, dr, power):
        self.num = num
        self.x = x
        self.y = y
        self.dr = dr
        self.power = power
        self.gun = 0
        self.point = 0

class Gun:
    def __init__(self, x, y, power):
        self.owner = 0
        self.x = x
        self.y = y
        self.power = power

def in_range(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False

def FIGHT(player, enemy):
    p_power = player.power + player.gun
    e_power = enemy.power + enemy.gun

    if p_power > e_power:
        winner = player
        loser = enemy
    elif p_power < e_power:
        winner = enemy
        loser = player
    else:
        if player.power > enemy.power:
            winner = player
            loser = enemy
        else:
            winner = enemy
            loser = player

    point = (winner.power + winner.gun) - (loser.power + loser.gun)
    return winner, loser, point

def CHANGE_GUN(player, x, y):
    #player가 [x, y]에 있는 총들 중에 바꿈

    #격자에 총이 많을 수 있음, 모든 총마다 그 자리에 있는지 확인하기
    candi = []
    for gun in guns:
        if gun.x == x and gun.y == y and gun.power > player.gun:
            candi.append(gun)

    #내가 가진 게 이미 제일 세면 나가기
    if len(candi) == 0:
        return

    #내가 가진 거 내려놓기
    for gun in guns:
        if gun.owner == player.num:
            gun.owner = 0
            gun.x, gun.y = x, y
            break

    #가장 공격력이 높은 총은 candi[0]
    candi.sort(key = lambda x: -x.power)
    target = candi[0]

    #총의 좌표 업데이트, 플레이어의 총 업데이트
    target.x, target.y = -1, -1
    target.owner = player.num
    player.gun = target.power

def LOSER_MOVE(loser):
    #내 방향으로 한 칸 가기
    #사람 있거나 격자 밖이면 오른쪽 90도 회전
    x, y = loser.x, loser.y

    while True:
        nx, ny = x + dx[loser.dr], y + dy[loser.dr]

        if not in_range(nx, ny) or where[nx][ny] != 0:
            loser.dr = (loser.dr + 1) % 4
        else:
            loser.x, loser.y = nx, ny
            where[nx][ny] = loser.num
            break

def LOSER(loser, x, y):
    #총 내려놓기
    for gun in guns:
        if gun.owner == loser.num:
            gun.owner = 0
            gun.x, gun.y = x, y
            break
    loser.gun = 0

    #한 칸 가기
    LOSER_MOVE(loser)

    #거기 총 있으면 총 교환
    CHANGE_GUN(loser, loser.x, loser.y)

def WINNER(winner, point, x, y):
    #포인트 획득
    winner.point += point

    #총 교환
    CHANGE_GUN(winner,x, y)

def BATTLE(player, x, y):
    for p in players:
        if p.x == x and p.y == y and p.num != player.num:
            enemy = p

    #player와 enemy가 [x, y]에서 싸움
    #winner, loser 정하기
    winner, loser, point = FIGHT(player, enemy)

    #진 사람은 거기에 총 내려놓기, 한 칸 가기, 총 교환
    LOSER(loser, x, y)

    #이긴 사람은 포인트 획득, 총 교환
    WINNER(winner, point, x, y)

    #이제 [x, y]에 있는 사람은 winner
    where[x][y] = winner.num

n, m, k = map(int, input().split())
#총 유무와 공격력
area = []
for i in range(n):
    area.append(list(map(int, input().split())))
guns = []
for row in range(n):
    for col in range(n):
        if area[row][col] != 0:
            gun = Gun(row, col, area[row][col])
            guns.append(gun)
#격자에 플레이어 있는지, 몇 번인지
where = []
for i in range(n):
    where.append([0] * n)
players = []
for i in range(1, m + 1):
    x, y, d, s = map(int, input().split())
    player = Player(i, x-1, y-1, d, s)
    players.append(player)
    where[x-1][y-1] = i

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

for turn in range(1, k + 1):
    #1번 플레이어부터 차례대로 이동
    for player in players:
        x, y = player.x, player.y
        where[x][y] = 0

        while True:
            nx, ny = x + dx[player.dr], y + dy[player.dr]

            if not in_range(nx, ny):
                player.dr = (player.dr + 2) % 4
            else:
                player.x, player.y = nx, ny
                break

        #거기 사람 있으면 싸우기
        if where[nx][ny] != 0:
            BATTLE(player, nx, ny)

        #거기 사람 없으면 총 바꿔
        else:
            CHANGE_GUN(player, nx, ny)
            #그 자리는 내 자리
            player.x, player.y = nx, ny
            where[x][y] = 0
            where[nx][ny] = player.num

for player in players:
    print(player.point, end = " ")