n = int(input())

area = []
for i in range(n):
    area.append(list(map(int, input().split())))

max_val = 0

for i in range(n):
    for j in range(n-2):
        for k in range(n):
            for m in range(n-2):
                if i != k or (i == k and j+2 < m):
                    max_val = max(max_val, area[i][j] + area[i][j+1] + area[i][j+2] + area[k][m] + area[k][m+1] + area[k][m+2])

print(max_val)