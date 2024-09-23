#각 폭탄당 1, 2, 3을 매칭시키고 다음 거 매칭시키고, ...
#만약 모든 폭탄 다 매치됐으면 총 초토화 개수 세기
#폭탄의 수를 미리 알아두면 좋을 듯?

def in_range(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False

def exploid(tmp, x, y, dx, dy):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not in_range(nx, ny):
            continue

        if tmp[nx][ny] == 0:
            tmp[nx][ny] = 2    

def bomb(tmp, index, x, y):
    if index == 1:
        dx, dy = [-2, -1, 1, 2], [0, 0, 0, 0]
    elif index == 2:
        dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    else:
        dx, dy = [-1, -1, 1, 1], [-1, 1, 1, -1]

    exploid(tmp, x, y, dx, dy)

def get_cnt(tmp):
    cnt = 0
    for row in range(n):
        for col in range(n):
            if tmp[row][col] != 0:
                cnt += 1
    return cnt


def game(cnt):
    if cnt == bomb_cnt + 1:
        tmp = []
        for i in range(n):
            tmp.append([0] * n)

        for row in range(n):
            for col in range(n):
                tmp[row][col] = area[row][col]

        for i in range(bomb_cnt):
            bomb(tmp, lst[i], bomb_pos[i][0], bomb_pos[i][1])
        
        global maxi
        maxi = max(maxi, get_cnt(tmp))

        return

    for i in range(1, 4):
        lst.append(i)
        game(cnt + 1)
        lst.pop()



lst = []

n = int(input())
area = []
for i in range(n):
    area.append(list(map(int, input().split())))

bomb_pos = []
for row in range(n):
    for col in range(n):
        if area[row][col] == 1:
            bomb_pos.append([row, col])
bomb_cnt = len(bomb_pos)

maxi = 0
game(1)

print(maxi)