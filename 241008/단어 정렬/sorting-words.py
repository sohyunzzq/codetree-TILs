n = int(input())
lst = []
for i in range(n):
    lst.append(input())

lst.sort()
for item in lst:
    print(item)