dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def in_range(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False

def move(row, col):
    x, y = row, col

    for i in range(4):
        if not in_range(x + dx[i], y + dy[i]):
            continue
        
        if grid[x+dx[i]][y+dy[i]] > grid[x][y]:
            return x + dx[i], y + dy[i]
    
    return -1, -1

#우선순위 상하좌우
#지금보다 더 크기만 하면 이동

n, row, col = map(int, input().split())
grid = []
for i in  range(n):
    grid.append(list(map(int, input().split())))

row -= 1
col -= 1

while True:
    print(grid[row][col], end = " ")
    row, col = move(row, col)
    if row == -1 and col == -1:
        break