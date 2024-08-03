n = int(input())

lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))

max_val = 0
for i in range(n):
    area = [0] * 1001

    for j in range(n):
        if i == j:
            continue
        for k in range(lst[j][0], lst[j][1]):
            area[k] = 1
    max_val = max(max_val, sum(area))

print(max_val)