def slide(dr):
    temp = []
    for i in range(4):
        temp.append([0] * 4)

    for col in range(3, -1, -1):
        index = 3
        for row in range(3, -1, -1):
            if grid[row][col] > 0:
                temp[index][col] = grid[row][col]
                index -= 1

    return temp    

def combine(dr):
    for col in range(4):
        for i in range(3, 0, -1):
            if grid[i][col] == 0:
                continue

            if grid[i][col] == grid[i-1][col]:
                grid[i][col] *= 2
                grid[i-1][col] = 0

    return grid

def rotate(dr, grid):
    for _ in range(dr):
        new_grid = []
        for i in range(4):
            new_grid.append([0] * 4)
    
        for i in range(4):
            for j in range(4):
                new_grid[i][j] = grid[3-j][i]

        grid = new_grid

    return grid



dict1 = {"D": 0, "L": 3, "U": 2, "R": 1}

grid = []
for i in range(4):
    grid.append(list(map(int, input().split())))
dr = dict1[input()]

#항상 아래로만 떨어지게 하기
#시계 방향으로 회전시킨 후 떨구고, 다시 돌려서 출력하기

#dict1[dr]만큼 시계 방향으로 회전시키고 떨구기

grid = rotate(dr, grid)
grid = slide(dr)
grid = combine(dr)
grid = slide(dr)
grid = rotate(4-dr, grid)


for row in grid:
    for col in row:
        print(col, end = " ")
    print()