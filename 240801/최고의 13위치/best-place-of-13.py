n = int(input())

area = []
for i in range(n):
    area.append(list(map(int, input().split())))

result = 0

for i in range(n):
    for j in range(n-2):
        temp = area[i][j] + area[i][j+1] + area[i][j+2]

        result = max(result, temp)

print(result)