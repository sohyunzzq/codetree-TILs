n, k = map(int, input().split())
lst = list(map(int, input().split()))

max_val = 0

for i in range(n-k):
    result = 0
    for j in range(i, i+k):
        result += lst[j]

    max_val = max(result, max_val)

print(max_val)