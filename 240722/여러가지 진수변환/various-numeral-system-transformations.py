N, B = map(int, input().split())

res = []
while N > B - 1:
    res.append(N % B)
    N //= B

res.append(N)

for i in res[::-1]:
    print(i, end = "")