n = int(input())

lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))

for x in range(1, 10000 + 1):
    ans = x
    check = True
    for j in range(n):
        x *= 2
        if lst[j][0] <= x <= lst[j][1]:
            continue
        else:
            check = False
            break
    if check:
        print(ans)