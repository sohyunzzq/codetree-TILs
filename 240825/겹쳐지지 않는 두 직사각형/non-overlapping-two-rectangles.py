import sys

def check(x1, y1, x2, y2, x3, y3, x4, y4):
    box = []
    for i in range(n):
        box.append([0] * m)

    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            box[i][j] += 1
    
    for i in range(x3, x4+1):
        for j in range(y3, y4+1):
            box[i][j] += 1
    
    for i in range(n):
        for j in range(m):
            if box[i][j] >= 2: #겹침
                return False 
    return True

def get_sum(x1, y1, x2, y2, x3, y3, x4, y4):
    sum1 = 0
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            sum1 += grid[i][j]
    for i in range(x3, x4+1):
        for j in range(y3, y4+1):
            sum1 += grid[i][j]
    
    return sum1

def make():
    maxi = -sys.maxsize
    for x1 in range(n):
        for y1 in range(m):
            for x2 in range(x1, n):
                for y2 in range(y1, m):
                    for x3 in range(n):
                        for y3 in range(m):
                            for x4 in range(x3, n):
                                for y4 in range(y3, m):
                                    if check(x1, y1, x2, y2, x3, y3, x4, y4):
                                        maxi = max(maxi, get_sum(x1, y1, x2, y2, x3, y3, x4, y4))
    return maxi

n, m = map(int, input().split())
grid = []
for i in range(n):
    grid.append(list(map(int, input().split())))

print(make())