n = int(input())

area = [0] * (20*n+1)
now = 10*n

for i in range(n):
    num, p = input().split()
    if p == "L":
        now -= int(num)
        for j in range(now-int(num), now):
            area[j] += 1
    else:
        now += int(num)
        for j in range(now, now+int(num)):
            area[j] += 1

area.sort(reverse=True)

cnt = 0
for i in area:
    if i < 2:
        break
    cnt += 1

print(cnt)