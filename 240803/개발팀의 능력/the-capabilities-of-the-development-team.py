lst = list(map(int, input().split()))

min_val = max(lst)
result = -1

t2 = []

for i in range(5):
    t1 = lst[i]
    for j in range(5):
        for k in range(j+1, 5):
            if j == i or k == i:
                continue
            t2.append(lst[j])
            t2.append(lst[k])

            sum1 = t1
            sum2 = sum(t2)
            sum3 = sum(lst) - sum1 - sum2

            if sum1 == sum2 or sum2 == sum3 or sum1 == sum3:
                t2 = []
                break
            
            min_val = min(min_val, abs(max(sum1, sum2, sum3) - min(sum1, sum2, sum3)))
            result = min_val
            t2 = []
print(result)