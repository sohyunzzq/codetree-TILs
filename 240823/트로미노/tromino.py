def tromino(x, y):
    maxi = 0
    for i in range(6):
        check = True
        cnt = 0
        for dx in range(0, 3):
            for dy in range(0, 3):
                if shapes[i][dx][dy] == 0:
                    continue
                
                if x + dx >= n or y + dy >= m:
                    check = False
                    break
                else:
                    cnt += area[x+dx][y+dy]
        
        if check:
            maxi = max(maxi, cnt)
    
    return maxi

ans = 0
n, m = map(int, input().split())
area = []
for i in range(n):
    area.append(list(map(int, input().split())))

shapes = [
    [[1, 1, 0],
    [1, 0, 0],
    [0, 0, 0]],

    [[1, 1, 0],
    [0, 1, 0],
    [0, 0, 0]],

    [[1, 0, 0],
    [1, 1, 0],
    [0, 0, 0]],

    [[0, 1, 0],
    [1, 1, 0],
    [0, 0, 0]],
    
    [[1, 1, 1],
    [0, 0, 0],
    [0, 0, 0]],
    
    [[1, 0, 0],
    [1, 0, 0],
    [1, 0, 0]]
]

for i in range(n):
    for j in range(m):
        ans = max(ans, tromino(i, j))

print(ans)