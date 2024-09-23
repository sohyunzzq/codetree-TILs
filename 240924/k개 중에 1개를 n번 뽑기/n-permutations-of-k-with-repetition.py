def choose(num):
    if num == n + 1:
        for digit in lst:
            print(digit, end = " ")
        print()
        return

    for i in range(1, k+1):
        lst.append(i)
        choose(num + 1)
        lst.pop()

k, n = map(int, input().split())
lst = []

choose(1)