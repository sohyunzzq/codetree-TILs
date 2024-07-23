n = int(input())

lst = []
for i in range(n):
    lst.append(int(input()))

cnt = 1
res = 0
for i in range(n):
    if i >= 1 and lst[i] * lst[i-1] > 0: #같은 부호
        cnt += 1
    else:
        cnt = 1
    res = max(res, cnt)

print(res)