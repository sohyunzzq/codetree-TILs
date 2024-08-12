n = int(input())
lst = list(map(int, input().split()))

for i in range(n):
    mini = lst[i]
    for j in range(i+1, n):
        if lst[j] < mini:
            mini = lst[j]
            index = j
    
            lst[i], lst[index] = lst[index], lst[i]

for num in lst:
    print(num, end = " ")