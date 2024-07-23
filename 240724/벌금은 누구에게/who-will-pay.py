n, m, k = map(int, input().split())

lst = [0] * (n+1)
num = []

for i in range(m):
    num.append(int(input()))

result = -1
for i in range(m):
    lst[num[i]] += 1
    if lst[num[i]] >= 3:
        result = num[i]
        break

print(result)