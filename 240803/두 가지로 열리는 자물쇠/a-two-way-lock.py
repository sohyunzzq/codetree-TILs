def check(x):
    if x == 1:
        return [n-1, n, 1, 2, 3]
    elif x == 2:
        return [n, 1, 2, 3, 4]
    elif x == n-1:
        return [n-3, n-2, n-1, n, 1]
    elif x == n:
        return [n-2, n-1, n, 1, 2]
    else:
        return [x-2, x-1, x, x+1, x+2]

n = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

ans = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):

            if (i in check(a1) and j in check(b1) and k in check(c1)) or (i in check(a2) and j in check(b2) and k in check(c2)):
                ans += 1

print(ans)