n = int(input())

down = n
up = 1

for i in range(n):
    if i % 2 == 0:  #짝수줄
        print("* " * down)
        down -= 1
    else:           #홀수줄
        print("* " * up)
        up += 1

up = int(n // 2) + 1
down = int(n//2)

if n % 2 == 0:
    for i in range(n):
        if i % 2 == 0:  #짝수줄
            print("* " * down)
            down -= 1
        else:           #홀수줄
            print("* " * up)
            up += 1
else:
    for i in range(n):
        if i % 2 == 1:  #홀수줄
            print("* " * down)
            down -= 1
        else:           #짝수줄
            print("* " * up)
            up += 1