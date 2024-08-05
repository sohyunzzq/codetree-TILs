n = int(input())
lst = list(map(int, input().split()))

ans = 100
for i in range(n):
    lst[i] *= 2 #i를 두 배

    for j in range(n): #j를 제거할 예정
        tmp = []
        for k in range(n):
            if j == k:
                continue
            tmp.append(lst[k])
        
        sum1 = 0
        for k in range(n-2):
            diff = abs(tmp[k] - tmp[k+1])
            sum1 += diff
        ans = min(ans, sum1)
    
    lst[i] //= 2

print(ans)