shapes = [
    [[1, 1, 1],
    [0, 0, 0],
    [0, 0, 0]],

    [[1, 0, 0],
    [1, 0, 0],
    [1, 0, 0],],

    [[1, 0, 0],
    [1, 1, 0],
    [0, 0, 0]],

    [[0, 1, 0],
    [1, 1, 0],
    [0, 0, 0]],

    [[1, 1, 0],
    [1, 0, 0],
    [0, 0, 0]],

    [[1, 1, 0],
    [0, 1, 0],
    [0, 0, 0]]
]

n, m = map(int, input().split())
area = []
for i in range(n):
    area.append(list(map(int, input().split())))

maxi = 0
for i in range(n):
    for j in range(m):
        for shape in shapes:
            tmp = 0
            for dx in range(0, 3):
                for dy in range(0, 3):
                    if shape[dx][dy] == 0:
                        continue
                    
                    if i + dx >= n or j + dy >= m:
                        break
                    else:
                        tmp += area[i+dx][j+dy]
            
            maxi = max(maxi, tmp)

print(maxi)