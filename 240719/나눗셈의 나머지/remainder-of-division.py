dict1 = {}
a, b = map(int, input().split())

while a > 1:
    if a % b in dict1:
        dict1[a % b] += 1
    else:
        dict1[a % b] = 1

    a //= b

total = 0
for val in dict1.values():
    total += val**2

print(total)