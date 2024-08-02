import sys

n, s = map(int, input().split())
lst = list(map(int, input().split()))

min_val = sys.maxsize

for i in range(n):
    for j in range(i+1, n):
        min_val = min(min_val, abs(s - (sum(lst) - lst[i] - lst[j])))
print(min_val)