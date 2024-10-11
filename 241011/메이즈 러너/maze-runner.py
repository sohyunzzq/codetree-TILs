class Runner:
    def __init__(self, x, y):
        self.escaped = False
        self.x = x
        self.y = y

def get_dist(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

def in_range(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False

def RUNNER_MOVE(runner):
    global ans
    dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]
    x, y = runner.x, runner.y

    curr_dist = get_dist(x, y, exitpos[0], exitpos[1])

    dists = []
    for dr in range(4):
        nx, ny = x + dx[dr], y + dy[dr]

        #움직였는데 격자 밖이거나 벽이면 그 방향은 안 됨
        if not in_range(nx, ny) or maze[nx][ny] != 0:
            continue

        dist = get_dist(nx, ny, exitpos[0], exitpos[1])
        if dist < curr_dist:
            #지금보다 가까워지는 게 확실하면 후보에 추가 [거리, dr]
            dists.append([dist, dr])

    #만약 갈 수 있는 곳이 없다면 그냥 나가
    if len(dists) == 0:
        return

    #이동 횟수 증가
    ans += 1

    #갈 수 있는 곳 하나 정하기
    dists.sort(key = lambda x: (x[0], x[1]))
    npos = dists[0]
    nx, ny = x + dx[npos[1]], y + dy[npos[1]]

    #만약 그 자리가 탈출구라면, 탈출 여부 업데이트, human 업데이트
    if [nx, ny] == exitpos:
        runner.escaped = True
        human[x][y] = 0
        return

    #human에서 기존 자리 없애기
    human[x][y] = 0

    #human에서 새로운 자리 업데이트, runner 좌표 업데이트
    human[nx][ny] += 1
    runner.x = nx
    runner.y = ny

def MAKE_SQUARE():
    #사람이 한 명 이상이고, 탈출구를 포함하는 정사각형들 모으기
    for i in range(2, n + 1):
        #처음 왼쪽 위 좌표 기준점
        x, y = exitpos[0] - i + 1, exitpos[1] - i + 1
        for j in range(i * i):
            #i*i개 네모에서 왼쪽 위
            row, col = x + j // i, y + j % i
            if not in_range(row, col):
                continue

            for xx in range(i):
                for yy in range(i):
                    if not in_range(row + xx, col + yy):
                        continue
                    if human[row + xx][col + yy] > 0:
                        return row, col, i

def ROTATE(x, y, size):
    #정사각형을 일일이 순회
    origin = []
    for i in range(size):
        origin.append([""] * size)

    for row in range(size):
        for col in range(size):
            tmp = ""
            tmp += str(x + row)
            tmp += str(y + col)
            origin[row][col] = tmp

    change = []
    for i in range(size):
        change.append([""] * size)

    for row in range(size):
        for col in range(size):
            change[row][col] = origin[col][size - row - 1]

    new_human = []
    for i in range(n):
        new_human.append([0] * n)

    for row in range(n):
        for col in range(n):
            new_human[row][col] = human[row][col]

    #이 부분은 다시 만들 거라 지워주기
    for row in range(x, x + size):
        for col in range(y, y + size):
            new_human[row][col] = 0

    for row in range(size):
        for col in range(size):
            #사람 있음
            if human[x + row][y + col] > 0:
                for runner in runners:
                    if runner.x == x + row and runner.y == y + col and not runner.escaped:
                        human[x + row][y + col] -= 1
                        runner.x = int(change[row][col][0])
                        runner.y = int(change[row][col][1])
                        new_human[runner.x][runner.y] += 1

    #새로 만든 배열 복제
    for row in range(x, x + size):
        for col in range(y, y + size):
            human[row][col] = new_human[row][col]

    #출구 좌표 업데이트
    nex, ney = 0, 0
    for row in range(size):
        for col in range(size):
            if exitpos[0] == x + row and exitpos[1] == y + col:
                nex = int(change[row][col][0])
                ney = int(change[row][col][1])
                break

    exitpos[0], exitpos[1] = nex, ney

    #새로운 미로판
    new_maze = []
    for i in range(n):
        new_maze.append([0] * n)

    for row in range(n):
        for col in range(n):
            new_maze[row][col] = maze[row][col]

    #돌리기
    for row in range(size):
        for col in range(size):
            new_maze[row + x][col + y] = maze[size - col - 1 + x][row + y]

    #내구도 감소
    for row in range(size):
        for col in range(size):
            if new_maze[row + x][col + y] > 0:
                new_maze[row + x][col + y] -= 1

    #새로 만든 미로 복제
    for row in range(n):
        for col in range(n):
            maze[row][col] = new_maze[row][col]

def ALL_ESCAPED():
    for runner in runners:
        if not runner.escaped:
            return False
    return True

n, m, k = map(int, input().split())
maze = []
for i in range(n):
    maze.append(list(map(int, input().split())))

human = []
for i in range(n):
    human.append([0] * n)

runners = []
for i in range(m):
    x, y = map(int, input().split())
    runners.append(Runner(x-1, y-1))
    human[x-1][y-1] += 1

x, y = map(int, input().split())
exitpos = [x-1, y-1]

ans = 0
for time in range(1, k + 1):
    #참가자 1번부터 m번까지 탈출 여부 검사 후 이동하기
    for runner in runners:
        if not runner.escaped:
            RUNNER_MOVE(runner)
            
    #전부 탈출했으면 종료
    if ALL_ESCAPED():
        break
        
    #다 움직인 후 정사각형 만듦, 왼쪽 위 좌표
    sq_x, sq_y, size = MAKE_SQUARE()

    #정사각형 회전, 내구도 감소시키기
    ROTATE(sq_x, sq_y, size)



print(ans)
print(exitpos[0] + 1, exitpos[1] + 1)