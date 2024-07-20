def cal(a, b):
    if a < b:
        return a * 2, b + 25
    return a + 25, b * 2

a, b = map(int, input().split())
a, b = cal(a, b)
print(a, b)