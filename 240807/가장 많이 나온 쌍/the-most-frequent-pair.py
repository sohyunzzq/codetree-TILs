n, m = map(int, input().split())

lst = []
for i in range(m):
    lst.append(list(map(int, input().split())))

ans = 0
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        cnt = 0
        for k in range(m):
            if (i == lst[k][0] and j == lst[k][1]) or (i == lst[k][1] and j == lst[k][0]):
                cnt += 1
        ans = max(cnt, ans)

print(ans)