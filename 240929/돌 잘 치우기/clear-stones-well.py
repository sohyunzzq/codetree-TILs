from collections import deque

n, k, m = map(int, input().split())
area = []
for i in range(n):
    area.append(list(map(int, input().split())))
coor = []
for i in range(k):
    x, y = map(int, input().split())
    coor.append([x-1, y-1])

stones = []
for row in range(n):
    for col in range(n):
        if area[row][col] == 1:
            stones.append([row, col])

def in_range(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False

def can_go(x, y):
    if in_range(x, y) and area[x][y] == 0 and not visited[x][y]:
        return True
    return False


def bfs():
    while q:
        tmp = q.popleft()
        x, y = tmp[0], tmp[1]

        dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
        for dr in range(4):
            nx, ny = x + dx[dr], y + dy[dr]

            if can_go(nx, ny):
                visited[nx][ny] = 1
                q.append([nx, ny])

ans = []
q = deque()

visited = []
for i in range(n):
    visited.append([0] * n)

def check():
    global visited
    global cnt

    for i in selected_stone:
        area[i[0]][i[1]] = 0

    ## 돌 설치 완료
    visited = []
    for i in range(n):
        visited.append([0] * n)

    for xy in coor:
        x, y = xy[0], xy[1]
        q.append([x, y])
    bfs()
    
    cnt = 0
    for row in visited:
        for col in row:
            if col == 1:
                cnt += 1
    ans.append(cnt)
    for i in selected_stone:
        area[i[0]][i[1]] = 1


#lst에 있는 돌들을 배치하고 세어보기
#lst에는, 좌표가 m개 있는 리스트가 1개 이상 -> 3중 배열



selected_stone = []
def select(pos):
    if pos == len(stones):
        if len(selected_stone) == m:
            check()
        return
    
    selected_stone.append(stones[pos])
    select(pos + 1)
    selected_stone.pop()

    select(pos + 1)

select(0)
print(max(ans))