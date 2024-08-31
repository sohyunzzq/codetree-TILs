def in_range(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False





def new_bomb(t):
    new_grid = []
    for i in range(n):
        new_grid.append([0] * n)

    for x in range(n):
        for y in range(n):
            if grid[x][y] == 1:
                new_grid[x][y] = 1

                for i in range(4):
                    new_x = x + dx[i] * (2 ** (t-1))
                    new_y = y + dy[i] * (2 ** (t-1))

                    if not in_range(new_x, new_y):
                        continue
                    
                    new_grid[new_x][new_y] = 1
    
    return new_grid


dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]



n, m, row, col = map(int, input().split())
grid = []
for i in range(n):
    grid.append([0] * n)

x = row-1
y = col-1

grid[x][y] = 1

for i in range(1, m+1):
    grid = new_bomb(i)

ans = 0
for i in range(n):
    ans += sum(grid[i])
print(ans)