n = int(input())
lst = [0] * (n * 100 * 2 + 1)

now = n * 100

for i in range(n):
    num, pos = input().split()
    if pos == "L":
        for j in range(now - int(num) + 1, now + 1):
            lst[j] = 1
        now = now - int(num) + 1
    else:
        for j in range(now, now + int(num)):
            lst[j] = 2
        now = now + int(num) - 1

w = 0
b = 0
for i in lst:
    if i == 1:
        w += 1
    elif i == 2:
        b += 1

print(w, b)
'''
흰 1 검 2
0 0 0 0 0 0 0 0 0 0
        s
        2 2 2 2
      1 1 1 1 1
      2 2 2 2 2 2 2
            1 1 1 1  
'''