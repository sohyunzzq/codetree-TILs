def triangle(coor1, coor2, coor3):
    x1 = coor1[0]
    y1 = coor1[1]
    x2 = coor2[0]
    y2 = coor2[1]
    x3 = coor3[0]
    y3 = coor3[1]

    if y1 == y2:
        if x1 == x3 or x2 == x3:
            return abs(x1-x2) * abs(y3-y1)
    elif y2 == y3:
        if x2 == x1 or x3 == x1:
            return abs(x2-x3) * abs(y1-y2)
    elif y3 == y1:
        if x3 == x2 or x1 == x2:
            return abs(x3-x1) * abs(y2-y1)
        
    return 0

n = int(input())

lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))

max_val = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            max_val = max(max_val, triangle(lst[i], lst[j], lst[k]))

print(max_val)