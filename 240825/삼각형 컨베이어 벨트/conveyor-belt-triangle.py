def shift(lst, tmp):
    for i in range(len(lst)-1, 0, -1):
        lst[i] = lst[i-1]
    lst[0] = tmp

n, t = map(int, input().split())
tri = []
for i in range(n):
    tri.append(list(map(int, input().split())))
t %= (3 * n)

for i in range(t):
    first = tri[0][n-1]
    second = tri[1][n-1]
    third = tri[2][n-1]

    shift(tri[0], third)
    shift(tri[1], first)
    shift(tri[2], second)

for item in tri[0]:
    print(item, end = " ")
print()
for item in tri[1]:
    print(item, end = " ")
print()
for item in tri[2]:
    print(item, end = " ")

'''
1 2 4 
5 9 3 
6 5 1

세 번째 줄 마지막 원소 third
두 번째 줄 마지막 원소 second
첫 번째 줄 마지막 원소 first

shift
'''