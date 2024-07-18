def compare(a, x):
    if a > x:
        print("1")
    else:
        print("0")

a = int(input())
b, c, d, e = map(int, input().split())

compare(a, b)
compare(a, c)
compare(a, d)
compare(a, e)