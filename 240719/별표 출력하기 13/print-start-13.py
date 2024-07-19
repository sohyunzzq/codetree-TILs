n = int(input())

even = n
odd = 1

for i in range(n*2):
    if i % 2 == 0:
        print("* " * even)
        even -= 1
    else:
        print("* " * odd)
        odd += 1