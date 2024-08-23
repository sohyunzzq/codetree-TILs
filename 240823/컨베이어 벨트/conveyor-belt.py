n, t = map(int, input().split())
cb = list(map(int, input().split()))
tmp = list(map(int, input().split()))
for item in tmp:
    cb.append(item)
t %= (2 * n)

for i in range(t):
    tmp = cb[2*n - 1]
    for j in range(2*n - 1, -1, -1):
        cb[j] = cb[j-1]
    cb[0] = tmp

for i in range(n):
    print(cb[i], end = " ")
print()
for i in range(n):
    print(cb[n+i], end = " ")