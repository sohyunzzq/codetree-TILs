month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

m1, d1, m2, d2 = map(int, input().split())
A = input()

for i in range(7):
    if A == day[i]:
        index = i

old = 0
new = 0

for i in range(m1):
    old += month[i]
old += d1

for i in range(m2):
    new += month[i]
new += d2

ans = (new-old) // 7
if index <= (new-old) % 7:
    ans += 1

print(ans)