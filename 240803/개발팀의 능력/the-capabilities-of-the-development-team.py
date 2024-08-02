lst = list(map(int, input().split()))

min_val = max(lst)
result = -1

t1 = []
t2 = []

for i in range(5):
    for j in range(i+1, 5):
        t1.append(lst[i])
        t1.append(lst[j])

        for k in range(5):
            for m in range(k+1, 5):
                if k == i or k == j or m == i or m == j:
                    continue
                t2.append(lst[k])
                t2.append(lst[m])

                sum1 = sum(t1)
                sum2 = sum(t2)
                sum3 = sum(lst) - sum1 - sum2

                if sum1 == sum2 or sum2 == sum3 or sum1 == sum3:
                    t2 = []
                    break
                
                min_val = min(min_val, abs(max(sum1, sum2, sum3) - min(sum1, sum2, sum3)))
                result = min_val
                t2 = []
        t1 = []

print(result)