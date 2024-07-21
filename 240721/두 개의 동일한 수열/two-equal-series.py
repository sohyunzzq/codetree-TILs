n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

if sorted(a) == sorted(b):
    print("Yes")
else:
    print("No")