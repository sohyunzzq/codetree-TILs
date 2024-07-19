def square(N):
    index = 1
    for i in range(N):
        for j in range(N):
            print(index, end = " ")
            index += 1
            if index > 9:
                index = 1
        print()

N = int(input())
square(N)