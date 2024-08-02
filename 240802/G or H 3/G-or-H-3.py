n, k = map(int, input().split())

lst = [0] * 10001
for i in range(n):
    num, alpha = input().split()
    lst[int(num)] = alpha

max_val = 0
for i in range(10001-k):
    result = 0
    for j in range(i, i+k+1):
        if lst[j] == "G":
            result += 1
        elif lst[j] == "H":
            result += 2
    max_val = max(max_val, result)

print(max_val)