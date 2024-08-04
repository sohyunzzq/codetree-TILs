t, a, b = map(int, input().split())

#S까지의 거리 <= N까지의 거리
#S    k        N

area = [0] * 1001
for i in range(t):
    c, x = input().split()
    area[int(x)] = c

cnt = 0
for i in range(a, b+1):
    s, n = 1001, 1001
    for j in range(1001):
        if area[j] == "S":
            s = min(s, abs(j-i))
        elif area[j] == "N":
            n = min(n, abs(j-i))
    
    if s <= n:
        cnt += 1
print(cnt)
'''
1 2 3 4 5 
  s     n

1 2 3 4 5 6 7 8 9 10
s     n            s
'''