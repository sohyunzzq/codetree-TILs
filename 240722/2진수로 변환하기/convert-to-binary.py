n = int(input())

res = []
while n > 1:
    res.append(n % 2)
    n //= 2

res.append(n)

for i in res[::-1]:
    print(i, end = "")