n, k = map(int, input().split())

basket = [0] * 101
for i in range(n):
    c, b = map(int, input().split())
    basket[b] = c

max_val = 0
for i in range(n):
    sum1 = 0
    for j in range(i, i + 2*k + 1):
        sum1 += basket[j]
    
    max_val = max(max_val, sum1)
print(max_val)