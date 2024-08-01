r, c = map(int, input().split())

area = []
for i in range(r):
    area.append(list(input().split()))

color = area[0][0]
cnt = 0

for i in range(1, r):
    for j in range(1, c):
        if area[i][j] != color:

            for k in range(i+1, r):
                for m in range(j+1, c):
                    if area[k][m] == color:

                        if area[r-1][c-1] != color and r-1 >= k + 1 and c-1 >= m + 1:
                            cnt += 1

print(cnt)