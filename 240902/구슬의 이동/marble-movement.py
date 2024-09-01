## 29분
## 어떤 걸 리턴할지 잘 판단하긔...
## global !!
## remove, pop 차이 기억하기: remove 값 자체, pop 인덱스


def in_range(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False


def remove_marble(row, col):
    ### 후보들을 모아보기
    candi = []
    for marble in marbles:
        if marble[1] == row and marble[2] == col:
            candi.append(marble)
    
    candi.sort(key = lambda x: (x[4], x[0]), reverse = True)

    while len(candi) != k:
        marbles.remove(candi.pop())
    
    return marbles


def game():
    grid = []
    for i in range(n):
        grid.append([0] * n)
    
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

    global marbles
    ### 그리드에 1초 후 구슬 개수 세기
    for marble in marbles:
        x, y = marble[1], marble[2]
        dr = marble[3]
        v = marble[4]

        for i in range(v):
            nx, ny = x + dx[dr], y + dy[dr]

            if not in_range(nx, ny):
                dr = (2 + dr) % 4
                nx, ny = x + dx[dr], y + dy[dr]
            
            x, y = nx, ny
        
        grid[nx][ny] += 1
        marble[1], marble[2] = nx, ny
        marble[3] = dr
    
        
    for row in range(n):
        for col in range(n):
            if grid[row][col] > k:
                marbles = remove_marble(row, col)
    
    return len(marbles)


mapper = {"U": 0, "R": 1, "D": 2, "L": 3}
n, m, t, k = map(int, input().split())
marbles = []
for i in range(1, m+1):
    r, c, d, v = input().split()
    marbles.append([i, int(r)-1, int(c)-1, mapper[d], int(v)])


for i in range(t):
    ans = game()

print(ans)