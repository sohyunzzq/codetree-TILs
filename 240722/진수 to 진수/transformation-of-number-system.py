a, b = input().split()
n = input()

d = 0

for i in range(len(n)):
    d = d * int(a) + int(n[i])

res = []
while d > int(b) - 1:
    res.append(d % int(b))
    d //= int(b)
res.append(d)

for i in res[::-1]:
    print(i, end = "")