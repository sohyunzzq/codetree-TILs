n, b = map(int, input().split())

lst = []
for i in range(n):
    lst.append(int(input()))
lst.sort()

max_val = 0
for i in range(n):
    cnt = 0
    temp = 0
    lst[i] //= 2
    for j in range(n):
        temp += lst[j]
        cnt += 1
        if temp <= b:
            max_val = max(max_val, cnt)
    lst[i] *= 2

print(max_val)