n = int(input())

lst = []
for i in range(n):
    lst.append(int(input()))

cnt = 1
res = 0
for i in range(n):
    if i == 0 or lst[i] != lst[i-1]:
        cnt = 1
    else:
        cnt += 1
    res = max(cnt, res)

print(res)