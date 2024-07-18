cnt = 0
n = int(input())

i = 1
while True:
    n //= i
    cnt += 1
    i += 1
    
    if n < 1:
        break

print(cnt)