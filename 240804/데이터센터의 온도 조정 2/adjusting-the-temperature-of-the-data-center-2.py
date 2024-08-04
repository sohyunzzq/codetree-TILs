n, c, g, h = map(int, input().split())

lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))

lst.sort(key = lambda x: x[1])

ans = 0
for i in range(lst[n-1][1]):
    temp = 0
    for j in range(n):
        if i < lst[j][0]:
            temp += c
        elif lst[j][0] <= i <= lst[j][1]:
            temp += g
        else:
            temp += h
    
    ans = max(ans, temp)

print(ans)