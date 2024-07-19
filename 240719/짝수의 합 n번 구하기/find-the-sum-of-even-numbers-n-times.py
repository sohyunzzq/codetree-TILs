n = int(input())

for i in range(n):
    sum1 = 0
    a, b = map(int, input().split())
    for j in range(a, b+1, 1):
        if j % 2 == 0:
            sum1 += j
    print(sum1)