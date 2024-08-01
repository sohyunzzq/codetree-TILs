import sys

n = int(input())

lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))

min_val = sys.maxsize

for i in range(1, n):
    tempx = lst[i][0]
    tempy = lst[i][1]

    lst[i][0] = lst[i-1][0]
    lst[i][1] = lst[i-1][1]

    result = 0
    for j in range(n-1):
        result += abs(lst[j+1][0] - lst[j][0]) + abs(lst[j+1][1] - lst[j][1])
    
    min_val = min(min_val, result)
    lst[i][0] = tempx
    lst[i][1] = tempy

print(min_val)