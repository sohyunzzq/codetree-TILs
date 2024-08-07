def jump(x):
    index = 0
    for i in range(1, n):
        if lst[i] <= x:
            if i - index > k:
                return False
            index = i
    return True
    
n, k = map(int, input().split())
lst = list(map(int, input().split()))

for i in range(max(lst[0], lst[n-1]), 100 + 1):
    if jump(i):
        print(i)
        break