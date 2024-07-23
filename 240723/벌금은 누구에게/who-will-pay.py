def check(k):
    for i in range(n+1):
        if lst[i] >= k:
            return i
    return False

n, m, k = map(int, input().split())

lst = [0] * (n+1)
for i in range(m):
    num = int(input())
    lst[num] += 1

    if check(k):
        print(check(k))
        break