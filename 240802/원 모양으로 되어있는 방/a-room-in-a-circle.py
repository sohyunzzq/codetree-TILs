import sys

min_val = sys.maxsize

n = int(input())

lst = []
for i in range(n):
    lst.append(int(input()))

for i in range(n):
    result = 0
    temp = lst[i]
    lst[i] = 0

    for j in range(n):
        val = j - i
        if val < 0:
            val += n
        result += val * lst[j]
    
    min_val = min(min_val, result)
    lst[i] = temp

print(min_val)