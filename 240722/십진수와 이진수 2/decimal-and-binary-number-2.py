b = input()

d = 0

for i in range(len(b)):
    d = d*2 + int(b[i])

d *= 17

res = []
while d > 1:
    res.append(d % 2)
    d //= 2

res.append(d)

for i in res[::-1]:
    print(i, end = "")