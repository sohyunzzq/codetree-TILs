n, t = map(int, input().split())
lst = list(map(int, input().split()))

res = 0
cnt = 0
for i in range(n):
    if lst[i] >= t:
        cnt += 1
    else:
        cnt = 0
    res = max(res, cnt)

print(res)