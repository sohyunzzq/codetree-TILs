n = int(input())
lst = list(map(int, input().split()))

lst.sort()
for item in lst:
    print(item, end = " ")
print()
lst.sort(reverse = True)
for item in lst:
    print(item, end = " ")
print()