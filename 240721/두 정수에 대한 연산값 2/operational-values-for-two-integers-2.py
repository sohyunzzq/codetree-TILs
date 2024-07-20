def cal(a, b):
    if a < b:
        return a + 10, b * 2
    return a * 2, b + 10

a, b = map(int, input().split())
a, b = cal(a, b)
print(a, b)