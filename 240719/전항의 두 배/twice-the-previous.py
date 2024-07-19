lst  = list(map(int, input().split()))

for i in range(8):
    lst.append(2*lst[i] + lst[i+1])

for i in lst:
    print(i, end = " ")