def check(k):
    for i in range(n+1):
        if lst[i] >= k:
            return i
    return -1

n, m, k = map(int, input().split())

lst = [0] * (n+1)
num = []

for i in range(m):
    num.append(int(input()))

for i in range(m):
    lst[num[i]] += 1
    result = check(k)
    if result > 0:
        print(result)
        break