n = int(input())
lst = list(map(int, input().split()))

for i in range(n):
    mini = i
    for j in range(i+1, n):
        if lst[j] < lst[mini]:
            mini = j
    
    lst[i], lst[mini] = lst[mini], lst[i]

for num in lst:
    print(num, end = " ")