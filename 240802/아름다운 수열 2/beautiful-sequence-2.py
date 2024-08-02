n, m = map(int, input().split())
lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))

cnt = 0
for i in range(n-m+1):
    for j in range(m):
        #00 01 02 / 10 11 12 / 20 21 22 / 
        # 0  1  2 /  1  2  3 /  2  3  4
        if lst1[i+j] not in lst2:
            break
        
        if j == m-1:
            cnt += 1

print(cnt)