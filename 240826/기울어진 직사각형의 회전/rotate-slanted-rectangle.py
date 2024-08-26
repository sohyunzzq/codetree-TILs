def rotate(r, c, m1, m2, m3, m4, direction):
    if direction == 0: #반시계 방향
        tmp = grid[r][c]
        
        #4번 방향
        for i in range(m4):
            grid[r-i][c-i] = grid[r-i-1][c-i-1]
        
        #3번 방향, 맨 아래 좌표는 r-m1, c-m1
        r, c = r-m4, c-m4
        for i in range(m3):
            grid[r-i][c+i] = grid[r-i-1][c+i+1]
        
        #2번 방향
        r, c = r-m3, c+m3
        for i in range(m2):
            grid[r+i][c+i] = grid[r+i+1][c+i+1]
        
        #1번 방향
        r, c = r+m2, c+m2
        for i in range(m1):
            grid[r+i][c-i] = grid[r+i+1][c-i-1]
        
        r, c = r+m1, c-m1
        grid[r-1][c+1] = tmp

    else: #시계 방향
        tmp = grid[r][c]
        
        #1번 방향, 맨 아래 좌표는 r-m1, c-m1
        for i in range(m1):
            grid[r-i][c+i] = grid[r-i-1][c+i+1]
        
        #2번 방향
        r, c = r-m1, c+m1
        for i in range(m2):
            grid[r-i][c-i] = grid[r-i-1][c-i-1]
        
        #3번 방향
        r, c = r-m2, c-m2
        for i in range(m3):
            grid[r+i][c-i] = grid[r+i+1][c-i-1]
        
        #4번 방향
        r, c = r+m3, c-m3
        for i in range(m4):
            grid[r+i][c+i] = grid[r+i+1][c+i+1]
        
        r, c = r+m4, c+m4
        grid[r-1][c-1] = tmp        




n = int(input())
grid = []
for i in range(n):
    grid.append(list(map(int, input().split())))
r, c, m1, m2, m3, m4, direction = map(int, input().split())
r = r - 1
c = c - 1

rotate(r, c, m1, m2, m3, m4, direction)

for row in grid:
    for col in row:
        print(col, end = " ")
    print()