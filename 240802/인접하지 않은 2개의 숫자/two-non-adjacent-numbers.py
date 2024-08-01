n = int(input())
lst = list(map(int, input().split()))

max_val = 0

for i in range(n):
    for j in range(i + 2, n):
        max_val = max(max_val, lst[i] + lst[j])

print(max_val)