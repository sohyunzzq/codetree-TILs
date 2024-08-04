n, k = map(int, input().split())

result = -1
bomb = []
for i in range(n):
    bomb.append(int(input()))

for i in range(n):
    b = bomb[i]
    for j in range(n):
        if i == j:
            continue
        
        if i - 3 <= j <= i + 3 and bomb[j] == b:
            result = max(result, bomb[j])

print(result)