#25분

#check를 계속 전달하지 말고, 전역으로 두고 매번 초기화하는 게 낫다
#check가 원본을 갖고 있을 이유도 없음. 그냥 터진 거 체크만 하면 된다.

#각 폭탄당 1, 2, 3을 매칭시키고 다음 거 매칭시키고, ...
#만약 모든 폭탄 다 매치됐으면 총 초토화 개수 세기
#폭탄의 수를 미리 알아두면 좋을 듯?

def in_range(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False

def exploid(x, y, dx, dy):
    check[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not in_range(nx, ny):
            continue

        check[nx][ny] = 1

def bomb(index, x, y):
    if index == 1:
        dx, dy = [-2, -1, 1, 2], [0, 0, 0, 0]
    elif index == 2:
        dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    else:
        dx, dy = [-1, -1, 1, 1], [-1, 1, 1, -1]

    exploid(x, y, dx, dy)

def get_cnt():
    cnt = 0
    for row in range(n):
        for col in range(n):
            if check[row][col] == 1:
                cnt += 1
    return cnt

def game(cnt):
    global maxi

    if cnt == bomb_cnt + 1:

        for row in range(n):
            for col in range(n):
                check[row][col] = 0

        for i in range(bomb_cnt):
            bomb(lst[i], bomb_pos[i][0], bomb_pos[i][1])
        
        maxi = max(maxi, get_cnt())
        return

    for i in range(1, 4):
        lst.append(i)
        game(cnt + 1)
        lst.pop()

n = int(input())
area = []
for i in range(n):
    area.append(list(map(int, input().split())))

lst = []
check = []
for i in range(n):
    check.append([0] * n)
    
bomb_pos = []
for row in range(n):
    for col in range(n):
        if area[row][col] == 1:
            bomb_pos.append([row, col])
bomb_cnt = len(bomb_pos)

maxi = 0
game(1)

print(maxi)