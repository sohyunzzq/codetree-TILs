dict1 = {"L": "R", "R": "L"}

def shift(lst, direction):
    if direction == "R":
        tmp = lst[0]
        for i in range(len(lst) - 1):
            lst[i] = lst[i+1]
        lst[m-1] = tmp
    else:
        tmp = lst[m-1]
        for i in range(len(lst) - 1, 0, -1):
            lst[i] = lst[i-1]
        lst[0] = tmp

def check(lst, lst2):
    for i in range(len(lst)):
        if lst[i] == lst2[i]:
            return True
    return False

def up(index, direction):
    while True:
        if index == 0:
            break
        
        if not check(grid[index], grid[index - 1]):
            break
        
        index -= 1
        direction = dict1[direction]
        shift(grid[index], direction)

def down(index, direction):
    while True:
        if index == n-1:
            break
        
        if not check(grid[index], grid[index + 1]):
            break
        
        index += 1
        direction = dict1[direction]
        shift(grid[index], direction)

n, m, q = map(int, input().split())
grid = []
for i in range(n):
    grid.append(list(map(int, input().split())))

for i in range(q):
    r, d = input().split()
    r = int(r) - 1

    shift(grid[r], d)

    up(r, d)
    down(r, d)

for row in grid:
    for col in row:
        print(col, end = " ")
    print()