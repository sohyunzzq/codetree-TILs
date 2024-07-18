a, b = map(int, input().split())

result = 1
for i in range(1, b+1):
    if i % a == 0:
        result *= i
print(result)