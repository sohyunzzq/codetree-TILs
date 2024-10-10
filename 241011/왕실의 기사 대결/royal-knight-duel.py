class Knight:
    def __init__(self, num, x, y, h, w, k):
        self.num = num
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.hp = k
        self.alive = True #살아 있으면 True
        self.attacked = False #밀렸으면 True
        self.damage = 0

def in_range(x, y):
    if 0 <= x < l and 0 <= y < l:
        return True
    return False

def in_range_extension(x, y, h, w):
    for row in range(x, x+h):
        for col in range(y, y+w):
            if not in_range(row, col):
                return False
    return True

def wall_extension(x, y, h, w):
    for row in range(x, x+h):
        for col in range(y, y+w):
            if area[row][col] == 2:
                return True
    return False

def noone(x, y, h, w, dr, my_num):
    for row in range(x, x+h):
        for col in range(y, y+w):
            nx, ny = row + dx[dr], col + dy[dr]
            someone = k_area[nx][ny]

            #그 누군가가 0이거나, 나면 ㄱㅊ
            if someone == 0 or someone == my_num:
                continue

            #누군가가 있는데 죽은 애면 ㄱㅊ
            for knight in knights:
                if knight.num == someone and not knight.alive:
                    continue

            return False
    return True

def CAN_GO(x, y, h, w):
    # 격자 밖으로 나가면 못 감
    if not in_range_extension(x, y, h, w):
        return False

    # 벽이 있으면 못 감
    if wall_extension(x, y, h, w):
        return False

    return True

def CAN_ATTACK(attacker, dr):
    #밀 수 있는지만 체크, 자리 업데이트x
    #어차피 한 방향으로만 밀릴 테니까...?
    copy = []
    for i in range(l):
        copy.append([0] * l)

    for row in range(l):
        for col in range(l):
            copy[row][col] = k_area[row][col]

    push = [attacker.num]
    while push:
        tmp = push.pop()
        for k in knights:
            if k.num == tmp:
                pusher = k
                break

        x, y = pusher.x, pusher.y
        h, w = pusher.h, pusher.w

        for row in range(x, x+h):
            for col in range(y, y+w):
                #현재 자리 지우기
                if copy[row][col] == pusher.num:
                    copy[row][col] = 0

        for row in range(x, x + h):
            for col in range(y, y + w):
                nx, ny = row + dx[dr], col + dy[dr]

                #격자 벗어나면 아무것도 못 움직임
                if not in_range(nx, ny):
                    return False

                someone = copy[nx][ny]
                #누군가를 찾았는데, 그게 0이면 ㄱㅊ
                if someone == 0:
                    pass

                #누군가를 찾았으면 추가하기
                else:
                    for knight in knights:
                        if knight.num == someone:
                            push.append(someone)
                            break

                #내 자리 표시해주기
                copy[nx][ny] = pusher.num

    #다 밀었음, 이제 벽이 있는지 검사, 하나라도 있으면 false
    for row in range(l):
        for col in range(l):
            if copy[row][col] != 0 and area[row][col] == 2:
                return False
    return True


def ATTACK(attacker, dr):
    #밀기
    #밀린 애는 밀렸다고 표시해주기
    push = [attacker.num]
    while push:
        tmp = push.pop()
        for k in knights:
            if k.num == tmp:
                pusher = k
                break

        #일단 공격 받은 애라고 표시, 최초 푸셔만 아니라고 표시해주기
        pusher.attacked = True
        x, y = pusher.x, pusher.y
        h, w = pusher.h, pusher.w

        for row in range(x, x + h):
            for col in range(y, y + w):
                #내 자리 지우기
                if k_area[row][col] == pusher.num:
                    k_area[row][col] = 0

        for row in range(x, x + h):
            for col in range(y, y + w):
                nx, ny = row + dx[dr], col + dy[dr]

                someone = k_area[nx][ny]
                #누군가를 찾았는데, 그게 0이면 ㄱㅊ
                if someone == 0:
                    pass

                #누군가를 찾았으면 추가하기
                for knight in knights:
                    if knight.num == someone:
                        push.append(someone)
                        break

                #내 자리 표시해주기
                k_area[nx][ny] = pusher.num

        pusher.x = x + dx[dr]
        pusher.y = y + dy[dr]

    attacker.attacked = False

def CAL():
    #밀린 애들 데미지 깎아주기
    for knight in knights:
        total = 0
        if knight.attacked:
            x, y = knight.x, knight.y
            h, w = knight.h, knight.w
            for row in range(x, x+h):
                for col in range(y, y+w):
                    if area[row][col] == 1:
                        total += 1
                        knight.hp -= 1

            # 데미지 계산 후 다시 상태 갱신해주기
            knight.attacked = False

            # 만약 체력이 0 이하면 죽었다고 표시
            if knight.hp <= 0:
                knight.alive = False
                knight.damage = 0

                #죽었으면 격자에서 흔적 지워주기
                for row in range(l):
                    for col in range(l):
                        if k_area[row][col] == knight.num:
                            k_area[row][col] = 0
            else:
                knight.damage += total

l, n, q = map(int, input().split())
area = []
for i in range(l):
    area.append(list(map(int, input().split())))
k_area = []
for i in range(l):
    k_area.append([0] * l)

#기사의 정보
knights = []
for i in range(1, n + 1):
    r, c, h, w, k = map(int, input().split())
    knights.append(Knight(i, r-1, c-1, h, w, k))
    for row in range(r-1, r-1+h):
        for col in range(c-1, c-1+w):
            k_area[row][col] = i

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

#커맨드, i번 기사를 dr 방향으로 한 칸 이동, dr은 북쪽부터 0~3
for _ in range(q):
    i, dr = map(int, input().split())

    #i번 기사를 찾고, 살아 있으면 움직이기
    for knight in knights:
        if knight.num == i and knight.alive:
            #움직일 건데, 격자 밖이 아니고, 벽도 아니고, 다른 기사도 없는 평범한 상황.
            #한 칸이 아니므로 모든 칸에 대해서 검사를 해주어야 함
            x, y = knight.x, knight.y
            h, w = knight.h, knight.w

            if not CAN_GO(x, y, h, w):
                continue

            #>>이동한 다음에<< 다른 기사가 있는지 확인
            #아무도 없거나 내 몸만 있으면 이동하기
            if noone(x, y, h, w, dr,knight.num):
                #기사 격자 위치를 다 지워주기
                for row in range(x, x+h):
                    for col in range(y, y+w):
                        k_area[row][col] = 0

                #이동한 후 위치로 업데이트
                nx, ny = x + dx[dr], y + dy[dr]
                knight.x, knight.y = nx, ny

                for row in range(x, x+h):
                    for col in range(y, y+w):
                        nx, ny = row + dx[dr], col + dy[dr]
                        k_area[nx][ny] = knight.num

            #다른 기사가 있다면
            else:
                if CAN_ATTACK(knight, dr):
                    ATTACK(knight, dr)

                    #전부 이동을 마침, 밀린 애들 데미지 깎고 저장해주기
                    CAL()

ans = 0
for knight in knights:
    ans += knight.damage
print(ans)