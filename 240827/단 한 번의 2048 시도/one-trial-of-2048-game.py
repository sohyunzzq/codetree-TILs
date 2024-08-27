def slide(dr):
    temp = []
    for i in range(4):
        temp.append([0] * 4)

    if dr == "U":
        for col in range(4):
            index = 0
            for row in range(4):
                if grid[row][col] > 0:
                    temp[index][col] = grid[row][col]
                    index += 1
    elif dr == "D":
        for col in range(3, -1, -1):
            index = 3
            for row in range(3, -1, -1):
                if grid[row][col] > 0:
                    temp[index][col] = grid[row][col]
                    index -= 1

    elif dr == "R":
        for row in range(3, -1, -1):
            index = 3
            for col in range(3, -1, -1):
                if grid[row][col] > 0:
                    temp[row][index] = grid[row][col]
                    index -= 1

    else:
        for row in range(4):
            index = 0
            for col in range(4):
                if grid[row][col] > 0:
                    temp[row][index] = grid[row][col]
                    index += 1

    return temp    

def combine(dr):
    if dr == "U":
        for col in range(4):
            for i in range(3):
                if grid[i][col] == 0:
                    continue

                if grid[i][col] == grid[i+1][col]:
                    grid[i][col] *= 2
                    grid[i+1][col] = 0

    elif dr == "D":
        for col in range(4):
            for i in range(3, 0, -1):
                if grid[i][col] == 0:
                    continue

                if grid[i][col] == grid[i-1][col]:
                    grid[i][col] *= 2
                    grid[i-1][col] = 0

    elif dr == "R":
        for row in range(4):
            for i in range(3, 0, -1):
                if grid[row][i] == 0:
                    continue

                if grid[row][i] == grid[row][i-1]:
                    grid[row][i] *= 2
                    grid[row][i-1] = 0

    else:
        for row in range(4):
            for i in range(3):
                if grid[row][i] == 0:
                    continue

                if grid[row][i] == grid[row][i+1]:
                    grid[row][i] *= 2
                    grid[row][i+1] = 0

    return grid





grid = []
for i in range(4):
    grid.append(list(map(int, input().split())))
dr = input()

grid = slide(dr)
grid = combine(dr)
grid = slide(dr)


for row in grid:
    for col in row:
        print(col, end = " ")
    print()