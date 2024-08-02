n, m = map(int, input().split())
lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))

dict1 = {}
for i in lst2:
    dict1[i] = 1

cnt = 0

for i in range(n-m+1):
    for j in range(m):
        if lst1[i+j] in dict1 and dict1[lst1[i+j]] != 0:
            dict1[lst1[i+j]] = 0
        else:
            for k in lst2:
                dict1[k] = 1
            break
    
    sum1 = 0
    for item in dict1:
        sum1 += dict1[item]
    if sum1 == 0:
        cnt += 1

    for j in lst2:
        dict1[j] = 1

print(cnt)