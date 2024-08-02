lst = list(map(int, input().split()))

min_val = max(lst)
for i in range(6):
    for j in range(i + 1, 6):
        for k in range(j + 1, 6):
            sum1 = lst[i] + lst[j] + lst[k]
            min_val = min(min_val, abs((sum(lst) - sum1) - sum1))

print(min_val)