n = int(input())

index = 0

for i in range(1, n+1):
    if i % 2 == 1:  #홀수줄
        for j in range(n):
            index += 1
            print(index, end = " ")
    else:
        for j in range(n):
            index += 2
            print(index, end = " ")
    print()