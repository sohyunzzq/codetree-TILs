k, n = map(int, input().split())

lst = []

def choose(pos):
    if pos == n:
        for item in lst:
            print(item, end = " ")
        print()

        return

    for i in range(1, k + 1):
        if pos == 0 or pos == 1 or not (lst[-1] == i and lst[-2] == i):
            lst.append(i)
            choose(pos + 1)
            lst.pop()

choose(0)