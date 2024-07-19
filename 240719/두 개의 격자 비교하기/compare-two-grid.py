n, m = map(int, input().split())

pan1 = []
pan2 = []
for i in range(n):
    pan1.append(list(map(int, input().split())))
for i in range(n):
    pan2.append(list(map(int, input().split())))

result = []
for i in range(n):
    result.append([])
    for j in range(m):
        result[i].append(0)

for i in range(n):
    for j in range(m):
        if pan1[i][j] != pan2[i][j]:
            result[i][j] = 1

for i in range(n):
    for j in range(m):
        print(result[i][j], end = " ")
    print()