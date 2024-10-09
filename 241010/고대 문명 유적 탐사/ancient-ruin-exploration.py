from collections import deque

k, m = map(int, input().split())
area = []
for i in range(5):
    area.append(list(map(int, input().split())))
wall = list(map(int, input().split()))

def rotate(area, x, y):
    #area 배열을 (x, y)를 기준으로 오른쪽으로 한 번 돌려라

    #리턴할 배열에 일단 area 복사하기
    new_area = []
    for i in range(5):
        new_area.append([0] * 5)

    for row in range(5):
        for col in range(5):
            new_area[row][col] = area[row][col]

    for row in range(3):
        for col in range(3):
            new_area[x + row - 1][y + col - 1] = area[x + 3-col-1 - 1][y + row - 1]

    return new_area

def in_range(x, y):
    if 0 <= x < 5 and 0 <= y < 5:
        return True
    return False

def can_go(x, y, area):
    if in_range(x, y) and not visited[x][y] and area[x][y] == num:
        return True
    return False

num = 0
def bfs(area):
    global visited
    global cnt
    global num

    while q:
        x, y = q.popleft()
        num = area[x][y]

        dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
        for dr in range(4):
            nx, ny = x + dx[dr], y + dy[dr]

            if can_go(nx, ny, area):
                cnt += 1
                visited[nx][ny] = 1
                q.append([nx, ny])

visited = []
q = deque()
cnt = 0
def GET_MAXI_SCORE(area):
    global visited
    global cnt
    global q
    ans = 0

    visited = []
    for i in range(5):
        visited.append([0] * 5)

    for row in range(5):
        for col in range(5):
            cnt = 1
            visited[row][col] = 1

            q = deque()
            q.append([row, col])
            bfs(area)

            if cnt >= 3:
                ans += cnt

    return ans

def GET_CASE(x, y):
    max_score = 0
    rotation = 0

    #현재의 x, y에서 쓸 배열
    tmp_area = []
    for i in range(5):
        tmp_area.append([0] * 5)

    for row in range(5):
        for col in range(5):
            tmp_area[row][col] = area[row][col]

    #총 3번 회전할 것임
    for i in range(1, 4):
        tmp_area = rotate(tmp_area, x, y)

        score = GET_MAXI_SCORE(tmp_area)
        if score > max_score:
            max_score = score
            rotation = i

    return [max_score, rotation, [x, y]]

def GET_FIRST():
    #[최대 가치, 회전 횟수, [row, col]]
    everycase = []

    #중심은 (1, 1) ~ (3, 3)
    for row in range(1, 4):
        for col in range(1, 4):
            everycase.append(GET_CASE(row, col))

    everycase.sort(key = lambda x: (-x[0], x[1], x[2][0], x[2][1]))

    return everycase[0]

def bfs2(area):
    global visited
    global erase_lst
    global cnt
    global num

    while q:
        x, y = q.popleft()
        num = area[x][y]

        dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
        for dr in range(4):
            nx, ny = x + dx[dr], y + dy[dr]

            if can_go(nx, ny, area):
                visited[nx][ny] = 1
                cnt += 1
                erase_lst[nx][ny] = 1
                q.append([nx, ny])

erase_lst = []
def ERASE(area):
    global visited
    global q
    global erase_lst
    global cnt

    visited = []
    for i in range(5):
        visited.append([0] * 5)

    empty_space = []
    for row in range(5):
        for col in range(5):
            cnt = 1
            visited[row][col] = 1

            erase_lst = []
            for i in range(5):
                erase_lst.append([0] * 5)

            q = deque()
            q.append([row, col])
            erase_lst[row][col] = 1

            bfs2(area)

            if cnt >= 3:
                for i in range(5):
                    for j in range(5):
                        if erase_lst[i][j] == 1:
                            empty_space.append([i, j])
                            area[i][j] = 0

    return area, empty_space

ans = []
index = 0
for turn in range(k):
    #1차 유물 획득
    case = GET_FIRST()
    if case[0] == 0:
        break
    ans.append(0)

    #유물 빈 공간 만들기
    rotation = case[1]
    for i in range(rotation):
        area = rotate(area, case[2][0], case[2][1])

    while True:
        area, empty_space = ERASE(area)
        ans[turn] += len(empty_space)

        if empty_space == []:
            break

        empty_space.sort(key = lambda x: (x[1], -x[0]))

        #빈 공간 채우기
        for i in range(len(empty_space)):
            x, y = empty_space[i][0], empty_space[i][1]

            area[x][y] = wall[index]
            index += 1

for item in ans:
    print(item, end = " ")