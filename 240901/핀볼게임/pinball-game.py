def in_range(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False


def set_dr(dr, x, y):
    ### / 모양
    if grid[x][y] == 1:
        if dr == 0:
            dr = 1
        elif dr == 1:
            dr = 0
        elif dr == 2:
            dr = 3
        else:
            dr = 2
    ### \ 모양
    elif grid[x][y] == 2:
        dr = 3 - dr

    return dr


def game(dr, x, y):
    ### 기본 세팅
    t = 1
    dx, dy = [1, 0, -1, 0], [0, -1, 0, 1] #하 좌 상 우

    while True:
        dr = set_dr(dr, x, y)
        x += dx[dr]
        y += dy[dr]
        t += 1

        if not in_range(x, y):
            return t


####### 입력받기
n = int(input())
grid = []
for i in range(n):
    grid.append(list(map(int, input().split())))


###### 기본 세팅
t = 0
x, y = 0, 0
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]


####### 모든 경우 구하기
for dr in range(4):
    for j in range(n):
        t = max(t, game(dr, x, y))

        if not in_range(x + dx[dr], y + dy[dr]):
            break
        
        x += dx[dr]
        y += dy[dr]


print(t)