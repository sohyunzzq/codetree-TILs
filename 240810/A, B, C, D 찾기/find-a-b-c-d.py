lst = list(map(int, input().split()))

lst.sort()
a = lst[0]
b = lst[1]
c = lst[2]
maxi = lst[-1]

print(a, b, c, maxi-a-b-c)