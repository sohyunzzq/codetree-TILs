def get_end(start, col):
    for i in range(start + 1, n):
        if grid[start][col] != grid[i][col]:
            return i - 1
    return n-1

def bomb(grid):
    for col in range(n):
        for start in range(n):
            if grid[start][col] == 0:
                continue
            
            end = get_end(start, col)

            cnt = end - start + 1
            if cnt >= m:
                for i in range(start, end + 1):
                    grid[i][col] = 0
    return grid

def drop(grid):
    temp = []
    for i in range(n):
        temp.append([0] * n)

    for col in range(n):
        index = n-1
        for row in range(n-1, -1, -1):
            if grid[row][col] != 0:
                temp[index][col] = grid[row][col]
                index -= 1
    return temp

def rotate(grid):
    temp = []
    for i in range(n):
        temp.append([0] * n)
    
    for row in range(n):
        for col in range(n):
            temp[row][col] = grid[n-col-1][row]
    return temp

n, m, k = map(int, input().split())
grid = []
for i in range(n):
    grid.append(list(map(int, input().split())))

for i in range(k):
    grid = bomb(grid)
    grid = drop(grid)

    while True:
        grid2 = bomb(grid)
        grid2 = drop(grid2)

        if grid == grid2:
            grid = grid2
            break

        grid = grid2
    grid = rotate(grid)
    grid = drop(grid)


while True:
    grid2 = bomb(grid)
    grid2 = drop(grid2)

    if grid == grid2:
        grid = grid2
        break

    grid = grid2


cnt = 0
for row in grid:
    for col in row:
        if col != 0:
            cnt += 1

print(cnt)