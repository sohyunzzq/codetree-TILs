def in_range(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False


def move(hx, hy):
    if apple[hx][hy]:
        ### 사과 없애기
        apple[hx][hy] = 0
    else:
        ### 사과 없으면 꼬리(맨 마지막) 줄어듦
        snake.pop()


    ### 머리가 이미 있으면 꼬이게 됨
    if [hx, hy] in snake:
        return False

    snake.insert(0, [hx, hy])
    return True


####### 머리 이동시키고 격자 벗어나는지 확인
def game(dr, p):
    global t
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

    for i in range(p):
        t += 1
        hx, hy = snake[0]
        
        ### 격자 벗어남
        if not in_range(hx + dx[dr], hy + dy[dr]):
            return False
        
        hx += dx[dr]
        hy += dy[dr]

        if not move(hx, hy):
            return False
    
    return True


####### 기본 세팅
n, m, k = map(int, input().split())
grid = []
apple = []
for i in range(n):
    grid.append([0] * n)
    apple.append([0] * n)
for i in range(m):
    x, y = map(int, input().split())
    apple[x-1][y-1] = 1

mapper = {"U": 0, "R": 1, "D": 2, "L": 3}
snake = [[0, 0]]
t = 0


####### 명령 받고 시뮬 돌리기
for i in range(k):
    dr, p = input().split()
    dr = mapper[dr]
    p = int(p)

    if not game(dr, p):
        break

print(t)