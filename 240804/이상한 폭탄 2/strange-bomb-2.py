n, k = map(int, input().split())

result = -1
bomb = []
for i in range(n):
    bomb.append(int(input()))

explode = [0] * n
for i in range(n):
    b = bomb[i]
    for j in range(n):
        if i == j:
            continue
        
        if i - k <= j <= i + k and bomb[j] == b:
            result = max(result, b)
print(result)