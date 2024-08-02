import sys

n, s = map(int, input().split())
lst = list(map(int, input().split()))

min_val = sys.maxsize

for i in range(n):
    for j in range(i+1, n):
        temp1 = lst[i]
        temp2 = lst[j]
        lst[i], lst[j] = 0, 0
        min_val = min(min_val, abs(s - sum(lst)))
        lst[i] = temp1
        lst[j] = temp2
print(min_val)