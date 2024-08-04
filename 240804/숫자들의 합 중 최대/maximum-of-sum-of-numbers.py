x, y = map(int, input().split())

max_val = 0

for num in range(x, y+1):
    num = str(num)
    temp = 0
    for i in range(len(num)):
        temp += int(num[i])
    max_val = max(max_val, temp)

print(max_val)