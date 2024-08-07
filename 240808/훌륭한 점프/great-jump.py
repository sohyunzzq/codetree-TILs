def jump(x):
    tmp = [0, n-1]
    for index, item in enumerate(lst):
        if item <= x and index not in tmp:
            tmp.append(index)
    tmp.sort()
    
    for i in range(len(tmp) - 1):
        if tmp[i+1] - tmp[i] > k:
            return False
    
    maxi = 0
    for i in range(len(tmp)):
        maxi = max(maxi, lst[tmp[i]])
    return maxi

n, k = map(int, input().split())
lst = list(map(int, input().split()))

ans = 100
for i in range(n):
    if jump(lst[i]):
        ans = min(ans, jump(lst[i]))
print(ans)