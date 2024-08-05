n, m = map(int, input().split())
lst = list(map(int, input().split()))

ans = 0
for i in range(n): #i번부터 시작
    temp = 0
    start = i

    for j in range(m):
        temp += lst[start - 1]
        start = lst[start - 1]
    
    ans = max(ans, temp)

print(ans)