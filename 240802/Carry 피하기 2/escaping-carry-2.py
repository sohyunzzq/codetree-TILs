n = int(input())

lst = []
for i in range(n):
    lst.append(int(input()))

result = -1

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if lst[i] % 10 + lst[j] % 10 + lst[k] % 10 >= 10:
                continue
            if lst[i] % 100 + lst[j] % 100 + lst[k] % 100 >= 100:
                continue
            if lst[i] % 1000 + lst[j] % 1000 + lst[k] % 1000 >= 1000:
                continue
            if lst[i] % 10000 + lst[j] % 10000 + lst[k] % 10000 >= 10000:
                continue
            result = max(result, lst[i] + lst[j] + lst[k])
print(result)