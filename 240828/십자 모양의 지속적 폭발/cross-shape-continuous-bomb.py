def in_range(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False

def select_row(col):
    for i in range(n):
        if grid[i][col] != 0:
            return i #선택한 열의 맨 위 인덱스
    return -1

def bomb(row, col):
    num = grid[row][col] #사방을 num개 터뜨리면 됨
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

    grid[row][col] = 0

    if num == 1: #내 것만 터뜨리고 걍 나가기
        return grid

    for i in range(4): #위부터 시계 방향
        x, y = row, col
        for j in range(num-1):
            if not in_range(x + dx[i], y + dy[i]):
                break
            
            x += dx[i]
            y += dy[i]
            grid[x][y] = 0
    return grid
    
def drop(grid):
    temp = []
    for i in range(n):
        temp.append([0] * n)

    for col in range(n):
        index = n-1
        for i in range(n-1, -1, -1):
            if grid[i][col] != 0:
                temp[index][col] = grid[i][col]
                index -= 1
    
    return temp









n, m = map(int, input().split())
grid = []
for i in range(n):
    grid.append(list(map(int, input().split())))

for i in range(m):
    col = int(input()) - 1

    row = select_row(col)
    if row == -1:
        continue

    grid = bomb(row, col)
    grid = drop(grid)

for row in grid:
    for col in row:
        print(col, end = " ")
    print()