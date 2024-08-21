n, m = map(int, input().split())
lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))

ans = 0
num = 0
cnt = 1
for i in range(n):
    for j in range(n):
        if num == lst[i][j]:
            cnt += 1
        else:
            num = lst[i][j]
            cnt = 1
    if cnt >= m:
        ans += 1

num = 0
cnt = 1
for i in range(n):
    for j in range(n):
        if num == lst[j][i]:
            cnt += 1
        else:
            num = lst[j][i]
            cnt = 1
    if cnt >= m:
        ans += 1

print(ans)