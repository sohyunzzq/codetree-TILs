import sys

min_val = sys.maxsize

n = int(input())

lst = []
for i in range(n):
    lst.append(int(input()))

for i in range(n):
    result = 0
    for j in range(n):
        result += (j - i + n) % n * lst[j]
    
    min_val = min(min_val, result)
print(min_val)