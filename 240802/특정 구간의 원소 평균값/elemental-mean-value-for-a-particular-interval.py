n = int(input())
lst = list(map(int, input().split()))

ans = 0
for i in range(n):
    for j in range(i, n):
        temp = []
        #ij 00 01 02 03 04 11 12 13 14 22
        for k in range(i, j+1):
            temp.append(lst[k])
        
        if (sum(temp) / len(temp)) in temp:
            ans += 1

print(ans)