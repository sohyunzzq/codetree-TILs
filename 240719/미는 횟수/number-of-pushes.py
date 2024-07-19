a = input()
b = input()

cnt = 0
for i in range(len(a) - 1):
    a = a[len(a)-1]+a[0:len(a)-1]
    cnt += 1 
    if a == b:
        print(cnt)
        break

if cnt == len(a) - 1:
    print(-1)