lst = list(map(int, input().split()))

t1 = []
t2 = []

min_val = max(lst)
for i in range(6):
    for j in range(i+1, 6):
        t1.append(lst[i])
        t1.append(lst[j])
        
        for m in range(6):
            for n in range(m+1, 6):
                if m == i or m == j or n == i or n == j:
                    continue
                t2.append(lst[m])
                t2.append(lst[n])

                min_val = min(min_val, abs(max(sum(t1), sum(t2), sum(lst)-sum(t1)-sum(t2)) - min(sum(t1), sum(t2), sum(lst)-sum(t1)-sum(t2))))
                t2 = []
        t1 = []

print(min_val)