def lcm(n, m):
    for i in range(max(n, m), n*m+1, max(n, m)):
        if i % n == 0:
            print(i)
            return

n, m = map(int, input().split())

lcm(n, m)