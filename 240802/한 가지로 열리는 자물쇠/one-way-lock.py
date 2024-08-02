n = int(input())
a, b, c = map(int, input().split())

ans = n ** 3

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            if i > a + 2 and j > b + 2 and k > c + 2:
                ans -= 1
print(ans)