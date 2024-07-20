def check(a, b):
    for i in range(len(a)):
        if i > len(a) - len(b):
            return False
        if a[i:i+len(b)] == b:
            return True

n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

if check(a, b):
    print("Yes")
else:
    print("No")