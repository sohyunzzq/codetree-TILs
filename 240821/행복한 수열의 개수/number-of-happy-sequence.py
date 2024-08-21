n, m = map(int, input().split())
lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))

ans = 0

cnt = 0
for i in range(n):
    num = lst[i][0]
    cnt = 1
    for j in range(1, n):
        if lst[i][j] == num:
            cnt += 1
            if cnt == m:
                ans += 1
        else:
            num = lst[i][j]
            cnt = 1
    
for i in range(n):
    num = lst[0][i]
    cnt = 1
    for j in range(1, n):
        if lst[j][i] == num:
            cnt += 1
            if cnt == m:
                ans += 1
        else:
            num = lst[i]
            cnt = 1

print(ans)
'''
1 2 3 4 5
1 4 4
1 5 6
'''