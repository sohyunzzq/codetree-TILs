import sys

n, h, t = map(int, input().split())
lst = list(map(int, input().split()))

min_val = sys.maxsize

for i in range(n - t + 1):
    cost = 0
    for j in range(t):
        cost += abs(h-lst[i+j])
    
    min_val = min(min_val, cost)

print(min_val)