n, k = map(int, input().split())

lst = []
for i in range(n):
    lst.append(int(input()))

ans = 0
#k가 3이면 [1, 4], [2, 5], ..., [9997 ,10000]
for i in range(1, 10000-k+1):
    tmp = 0
    for num in lst:
        if i <= num <= i+k:
            tmp += 1
    ans = max(ans, tmp)

print(ans)