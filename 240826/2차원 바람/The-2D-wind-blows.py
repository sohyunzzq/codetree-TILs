def in_range(x, y):
    if 0 <= x < n and 0 <= y < m:
        return True
    return False

def shift(x1, y1, x2, y2):
    tmp = grid[x1][y1]

    for i in range(x2 - x1): #왼쪽
        grid[x1+i][y1] = grid[x1+i+1][y1]
    
    for i in range(y2 - y1): #아래
        grid[x2][y1+i] = grid[x2][y1+i+1]

    for i in range(x2 - x1): #오른쪽
        grid[x2-i][y2] = grid[x2-i-1][y2]

    for i in range(y2 - y1): #위
        grid[x1][y2-i] = grid[x1][y2-i-1]

    grid[x1][y1+1] = tmp

def make_num(x, y):
    cnt = 1
    sum1 = grid[x][y]

    if in_range(x+1, y):
        sum1 += grid[x+1][y]
        cnt += 1

    if in_range(x, y+1):
        sum1 += grid[x][y+1]
        cnt += 1

    if in_range(x-1, y):
        sum1 += grid[x-1][y]
        cnt += 1

    if in_range(x, y-1):
        sum1 += grid[x][y-1]
        cnt += 1

    
    return sum1 // cnt


def edit(x1, y1, x2, y2):
    for i in range(x2-x1+1):
        for j in range(y2-y1+1):
            new_grid[x1+i][y1+j] = make_num(x1+i, y1+j)


n, m, q = map(int, input().split())
grid = []
new_grid = []
for i in range(n):
    grid.append(list(map(int, input().split())))
    new_grid.append([0] * m)

for i in range(n):
    for j in range(m):
        new_grid[i][j] = grid[i][j]

for i in range(q):
    r1, c1, r2, c2 = map(int, input().split())
    r1, c1, r2, c2 = r1-1, c1-1, r2-1, c2-1

    shift(r1, c1, r2, c2)
    edit(r1, c1, r2, c2)

    for i in range(n):
        for j in range(m):
            grid[i][j] = new_grid[i][j]

for row in grid:
    for col in row:
        print(col, end = " ")
    print()