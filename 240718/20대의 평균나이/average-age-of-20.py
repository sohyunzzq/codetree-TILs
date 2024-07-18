sum1 = 0
cnt = 0

while True:
    age = int(input())
    if age < 20 or age >= 30:
        break
    sum1 += age
    cnt += 1

print("{:.2f}".format(sum1/cnt))