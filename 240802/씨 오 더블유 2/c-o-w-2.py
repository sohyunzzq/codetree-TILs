n = int(input())
a = input()

cnt = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if a[i] == "C" and a[j] == "O" and a[k] == "W":
                cnt += 1
print(cnt)