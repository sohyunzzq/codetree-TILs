n, t = map(int, input().split())
lst = list(map(int, input().split()))

res = 0
for i in range(n):
    if i >= 1 and lst[i] > t and lst[i-1] > t and lst[i] > lst[i-1]:
        cnt += 1
    else:
        cnt = 1

    res = max(res, cnt)

print(res)