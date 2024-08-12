n = int(input())
lst = list(map(int, input().split()))

maxi = max(lst)
leng = len(str(maxi))

for i in range(n):
    lst[i] = str(lst[i])

for i in range(1, leng+1):
    arr = []
    for j in range(10):
        arr.append([])
    
    for j in range(n):
        if i > len(lst[j]):
            num = 0
        else:
            num = int(lst[j][-i])
        arr[num].append(lst[j])
    
    tmp = []
    for j in range(10):
        for k in range(len(arr[j])):
            tmp.append(arr[j][k])
    
    lst = tmp

for i in range(n):
    print(int(lst[i]), end = " ")