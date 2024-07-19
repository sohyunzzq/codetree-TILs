n = int(input())

total = 0
for i in range(n):
    total += int(input())

result = str(total)
result = result[1:len(result)] + result[0]
print(result)