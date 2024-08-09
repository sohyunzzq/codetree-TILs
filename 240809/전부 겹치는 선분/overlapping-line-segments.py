def overlap():
    line1 = lst[0]
    for i in range(1, n):
        line2 = lst[i]

        if line1[1] < line2[0] or line2[1] < line1[0]:
            return False
        else:
            line1[0] = max(line1[0], line2[0])
            line2[1] = min(line1[1], line2[1])
    return True

n = int(input())

lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))

if overlap():
    print("Yes")
else:
    print("No")