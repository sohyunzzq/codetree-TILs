n = int(input())

lst = []
for i in range(n):
    a = int(input())
    if a > 0:
        lst.append(1)
    else:
        lst.append(-1)

cnt = 1
res = 0
for i in range(n):
    if i == 0 or lst[i] != lst[i-1]:
        cnt = 1
    else:
        cnt += 1
    res = max(res, cnt)

print(res)