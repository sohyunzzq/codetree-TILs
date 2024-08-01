import sys

n = int(input())
lst = list(map(int, input().split()))

min_val = sys.maxsize
for i in range(n):
    result = 0
    temp = lst[i]
    lst[i] = 0

    for j in range(n):
        result += lst[j] * abs(i-j)
    
    min_val = min(min_val, result)
    lst[i] = temp

print(min_val)