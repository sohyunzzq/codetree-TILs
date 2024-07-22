month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

m1, d1, m2, d2 = map(int, input().split())

old = 0
new = 0

for i in range(m1):
    old += month[i]
old += d1

for i in range(m2):
    new += month[i]
new += d2

result = new % 7 - old % 7

if 1 + result < 0:
    result += 7
if 1 + result > 6:
    result -= 7

print(day[1 + result])