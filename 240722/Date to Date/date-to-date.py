month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
m1, d1, m2, d2 = map(int, input().split())

total1 = 0
total2 = 0

for i in range(m1):
    total1 += month[i]
total1 += d1

for i in range(m2):
    total2 += month[i]
total2 += d2

print(total2 - total1 + 1)