N, K = map(int, input().split())

lst = [0] * N

for i in range(K):
    a, b = map(int, input().split())
    for j in range(a, b+1):
        lst[j] += 1

print(max(lst))