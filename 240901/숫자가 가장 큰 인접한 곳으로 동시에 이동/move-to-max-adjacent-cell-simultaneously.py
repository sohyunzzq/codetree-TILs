def in_range(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False


def move():
    new_count = []
    for i in range(n):
        new_count.append([0] * n)

    ### 구슬이 있으면 nc에 다음 위치를 표시해주기
    for row in range(n):
        for col in range(n):
            if count[row][col] == 1:
                maxi = -1
                maxx, maxy = -1, -1
                for dr in range(4):
                    nx, ny = row + dx[dr], col + dy[dr]
                    if not in_range(nx, ny):
                        continue
                    
                    if grid[nx][ny] > maxi:
                        maxi = grid[nx][ny]
                        maxx, maxy = nx, ny
                
                new_count[maxx][maxy] += 1

    
    ### 구슬 충돌한 거 삭제
    for row in range(n):
        for col in range(n):
            if new_count[row][col] >= 2:
                new_count[row][col] = 0
    
    ### 배열 카피
    for row in range(n):
        for col in range(n):
            count[row][col] = new_count[row][col]


####### 입력받기
n, m, t = map(int, input().split())
grid = []
count = []
for i in range(n):
    grid.append(list(map(int, input().split())))
    count.append([0] * n)
for i in range(m):
    x, y = map(int, input().split())
    count[x-1][y-1] = 1


dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


####### 시뮬
for i in range(t):
    move()

ans = 0
for row in range(n):
    ans += sum(count[row])
print(ans)