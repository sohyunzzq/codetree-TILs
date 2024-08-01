a = input()

cnt = 0
for i in range(len(a)):
    for j in range(i+1, len(a)):
        for k in range(j+1, len(a)):
            for m in range(k+1, len(a)):
                if a[i] == "(" and a[j] == "(" and i + 1 == j and a[k] == ")" and a[m] == ")" and k + 1 == m:
                    cnt += 1
print(cnt)