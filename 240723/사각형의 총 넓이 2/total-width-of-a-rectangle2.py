n = int(input())

pan = []
for i in range(201):
    pan.append([0]*201)

for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(x1, x2):
        for k in range(y1, y2):
            pan[j][k] = 1

cnt = 0
for i in range(201):
    for j in range(201):
        if pan[i][j] == 1:
            cnt += 1

print(cnt)