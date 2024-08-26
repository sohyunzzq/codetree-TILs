def in_range(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False

def bomb(r, c):
    num = grid[r][c] #몇 개가 터져야 하는지

    grid[r][c] = 0
    
    if num == 1:
        return grid

    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

    for i in range(4):
        x, y = r, c
        for j in range(num-1):
            if not in_range(x + dx[i], y + dy[i]):
                break
            
            x += dx[i]
            y += dy[i]

            grid[x][y] = 0   
    
    return grid

def pull():
    temp = []
    for i in range(n):
        temp.append([0] * n)

    for col in range(n):
        index = n-1
        for row in range(n-1, -1, -1):
            if grid[row][col] == 0:
                continue
            temp[index][col] = grid[row][col]
            index -= 1
    
    return temp
        



n = int(input())
grid = []
for i in range(n):
    grid.append(list(map(int, input().split())))
r, c = map(int, input().split())

grid = bomb(r-1, c-1)
grid = pull()

for row in grid:
    for col in row:
        print(col, end = " ")
    print()