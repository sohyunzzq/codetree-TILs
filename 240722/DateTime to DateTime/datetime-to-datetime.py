a, b, c = map(int, input().split())

total1 = 0
total2 = 0

total1 += 10*24*60 + 11*60 + 11
total2 += (a-1)*24*60 + b*60 + c

if total1 > total2:
    print(-1)
else:
    print(total2 - total1)