n, m = map(int, input().split())
lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))

check = []

for i in lst2:
    check.append([i, 1])

cnt = 0

for i in range(n-m+1):
    for j in range(m):
        for k in range(m):
            if lst1[i+j] == check[k][0] and check[k][1] != 0:
                check[k][1] = 0
                break
    sum1 = 0
    for j in check:
        sum1 += j[1]
    if sum1 == 0:
        cnt += 1

    for q in check:
        q[1] = 1

print(cnt)