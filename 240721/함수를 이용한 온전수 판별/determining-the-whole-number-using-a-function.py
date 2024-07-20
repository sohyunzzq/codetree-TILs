def check(n):
    if not (n % 2 == 0 or n % 10 == 5 or (n % 3 == 0 and n % 9 != 0)):
        return True
    return False

a, b = map(int, input().split())
cnt = 0

for i in range(a, b+1):
    if check(i):
        cnt += 1

print(cnt)