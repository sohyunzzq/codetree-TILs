n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

if a == b:
    print("Yes")
else:
    print("No")