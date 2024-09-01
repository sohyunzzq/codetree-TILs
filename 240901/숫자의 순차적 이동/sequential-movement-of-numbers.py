def in_range(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False

def exchange(x, y):
    #위부터 시계 방향으로 돌기
    dx, dy = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]
    maxi = -1
    maxx, maxy = -1, -1

    for dr in range(8):
        nx, ny = x + dx[dr], y + dy[dr]

        if not in_range(nx, ny):
            continue
        
        if grid[nx][ny] > maxi:
            maxi = grid[nx][ny]
            maxx, maxy = nx, ny

    grid[x][y], grid[maxx][maxy] = grid[maxx][maxy], grid[x][y]


def find_num(num):
    for row in range(n):
        for col in range(n):
            if grid[row][col] == num:
                exchange(row, col)
                return


def turn():
    for num in range(1, n * n + 1):
        find_num(num)


n, m = map(int, input().split())
grid = []
for i in range(n):
    grid.append(list(map(int, input().split())))

####### 시뮬
for i in range(m):
    turn()


for row in grid:
    for col in row:
        print(col, end = " ")
    print()