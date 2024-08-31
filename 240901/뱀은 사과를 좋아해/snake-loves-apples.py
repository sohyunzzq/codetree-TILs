def in_range(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False

def game(grid):
    t = 0
    head_x, head_y = 0, 0
    tail_x, tail_y = 0, 0  
    grid[head_x][head_y] = 2 #머리 2, 몸 1

    for i in range(k):
        dr = dict1[cmd[i][0]]
        p = int(cmd[i][1])
    
        for j in range(p):
            t += 1

            grid, head_x, head_y, tail_x, tail_y = move_snake(grid, dr, head_x, head_y, tail_x, tail_y)
            if grid == 0:
                return t


    return t

def move_snake(grid, dr, head_x, head_y, tail_x, tail_y):
    if not in_range(head_x + dx[dr], head_y + dy[dr]):
        return 0, 0, 0, 0, 0

    new_grid = []
    for i in range(n):
        new_grid.append([0] * n)
    
    head_x += dx[dr]
    head_y += dy[dr]

    for row in range(n):
        for col in range(n):
            if grid[row][col] == 1 or grid[row][col] == 2:
                new_grid[row][col] = 1
            elif grid[row][col] == "apple":
                new_grid[row][col] = "apple"

    if grid[head_x][head_y] == 1:
        return 0, 0, 0, 0, 0

    new_grid[head_x][head_y] = 2 #머리의 위치

    if grid[head_x][head_y] == "apple":
        pass
    else:
        new_grid[tail_x][tail_y] = 0

        tail_x += dx[dr]
        tail_y += dy[dr]

    return new_grid, head_x, head_y, tail_x, tail_y



dict1 = {"U": 0, "R": 1, "D": 2, "L": 3}
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

n, m, k = map(int, input().split())
grid = []
for i in range(n):
    grid.append([0] * n)
for i in range(m):
    x, y = map(int, input().split())
    grid[x-1][y-1] = "apple"



cmd = []
for i in range(k):
    cmd.append(input().split())

t = game(grid)


    

    

print(t)