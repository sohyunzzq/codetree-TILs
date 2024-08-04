n, b = map(int, input().split())

lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))

max_val = 0
for i in range(n):
    temp = 0
    cnt = 0
    lst[i][0] //= 2
    tmplst = sorted(lst, key = lambda x: x[0] + x[1])
    
    for j in range(n):
        temp += tmplst[j][0] + tmplst[j][1]
        cnt += 1
        if temp <= b:
            max_val = max(max_val, cnt)
    
    lst[i][0] *= 2

print(max_val)