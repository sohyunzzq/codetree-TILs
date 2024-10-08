from collections import deque

#가장 바깥 0 뭉텅이들을 검사해서 찾아내
#   바깥이랑 연결돼 있는 애들만 녹일 수 있음
#   연결 안 돼 있다는 건 빙하로 둘러쌓여 있다는 것
#찾아서 배열에 넣어두고, 다 찾았으면 배열에 있는 것들 하나하나 들르면서 주변 1을 0으로 만들기

n, m = map(int, input().split())
area = []
for i in range(n):
    area.append(list(map(int, input().split())))
visited = []
for i in range(n):
    visited.append([0] * m)

num_of_glagier = 0
for row in area:
    for col in row:
        if col == 1:
            num_of_glagier += 1

q = deque()

def in_range(x, y):
    if 0 <= x < n and 0 <= y < m:
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
                coor.append([nx, ny])

def melt():
    global cnt
    global num_of_glagier
    tmp = []
    for c in coor:
        x, y = c[0], c[1]

        dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
        for dr in range(4):
            nx, ny = x + dx[dr], y + dy[dr]

            if in_range(nx, ny) and area[nx][ny] == 1:
                area[nx][ny] = 0
                cnt += 1
                tmp.append([nx, ny])
                num_of_glagier -= 1

    for item in tmp:
        coor.append(item)
        
def all_melted():
    for row in range(n):
        for col in range(m):
            if area[row][col] == 1:
                return False
    return True

cnt = 0
t = 0
coor = [[0, 0]]
flag = 1

     
visited[0][0] = 1
q.append([0, 0])

bfs()

    #가장 바깥 0의 좌표들이 coor에 들어감
while num_of_glagier: 
    cnt = 0
    melt()
    t += 1

print(t, cnt)