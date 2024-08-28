def in_range(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False

def bomb(grid, row, col):
    num = grid[row][col] #num개 터뜨리기
    grid[row][col] = 0

    if num == 0:
        return grid
    
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    for i in range(0, 4): #사방
        x, y = row, col
        for _ in range(num - 1):
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
        for row in range(n-1, -1, -1):
            if grid[row][col] != 0:
                temp[index][col] = grid[row][col]
                index -= 1
    
    return temp

def pair(grid):
    cnt = 0
    for row in range(n):
        for col in range(n-1):
            if grid[row][col] == 0:
                continue

            if grid[row][col] == grid[row][col + 1]:
                cnt += 1
    
    for col in range(n):
        for row in range(n-1):
            if grid[row][col] == 0:
                continue
            
            if grid[row][col] == grid[row + 1][col]:
                cnt += 1
    
    return cnt





n = int(input())
grid = []
for i in range(n):
    grid.append(list(map(int, input().split())))

maxi = 0
for x in range(n):
    for y in range(n):
        temp = []
        for i in range(n):
            temp.append([0] * n)

        for row in range(n):
            for col in range(n):
                temp[row][col] = grid[row][col]

        temp = bomb(temp, x, y)
        temp = drop(temp)

        maxi = max(maxi, pair(temp))

print(maxi)