n, b = map(int, input().split())

lst = []
for i in range(n):
    lst.append(int(input()))

max_val = 0
for i in range(n):
    temp = lst[i] // 2
    cnt = 1
    for j in range(n):
        if i == j:
            continue
        temp += lst[j]
        cnt += 1
        if temp <= b:
            max_val = max(max_val, cnt)

print(max_val)