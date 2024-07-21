n = int(input())
lst = list(map(int, input().split()))

lst.sort()
for i in lst:
    print(i, end = " ")
print()
for i in lst[::-1]:
    print(i, end = " ")