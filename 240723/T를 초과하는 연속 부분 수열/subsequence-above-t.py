n, t = map(int, input().split())
lst = list(map(int, input().split()))

res = 0
for i in range(n):
    if lst[i] <= t:
        cnt = 0
    elif i >= 1:
        cnt += 1
    else:
        cnt = 1
    res = max(res, cnt)

print(res)