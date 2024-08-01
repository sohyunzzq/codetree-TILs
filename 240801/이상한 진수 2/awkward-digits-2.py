def bintodec(a):
    res = 0
    for i in range(len(a)):
        res *= 2
        res += a[i]
    return res

a = list(map(int, input()))

max_val = 0

for i in range(1, len(a)):
    temp = a[i]
    a[i] = (a[i] + 1) % 2

    max_val = max(max_val, bintodec(a))
    a[i] = temp

print(max_val)