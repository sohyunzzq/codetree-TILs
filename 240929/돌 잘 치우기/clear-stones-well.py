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
    if in_range(x, y) and new_area[x][y] == 0 and not visited[x][y]:
        return True
    return False


cnt = 0
def bfs():
    global cnt
    while q:
        tmp = q.popleft()
        x, y = tmp[0], tmp[1]

        dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
        for dr in range(4):
            nx, ny = x + dx[dr], y + dy[dr]

            if can_go(nx, ny):
                cnt += 1
                visited[nx][ny] = 1
                q.append([nx, ny])

ans = []
q = deque()

new_area = []
visited = []
for i in range(n):
    visited.append([0] * n)

def check():
    global new_area
    global visited
    global cnt
    new_area = []
    for i in range(n):
        new_area.append([0] * n)
    
    for row in range(n):
        for col in range(n):
            new_area[row][col] = area[row][col]

    for i in selected_stone:
        new_area[i[0]][i[1]] = 0

    
    ## 돌 설치 완료
    visited = []
    for i in range(n):
        visited.append([0] * n)

    for row in range(n):
        for col in range(n):
            if can_go(row, col):
                cnt = 1
                visited[row][col] = 1
                q.append([row, col])
                bfs()
            
                ans.append(cnt)
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