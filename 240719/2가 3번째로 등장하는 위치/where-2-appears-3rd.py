n = int(input())

lst = list(map(int, input().split()))

count = 0

for i in range(len(lst)):
    if lst[i] == 2:
        count += 1
    
    if count == 3:
        print(i+1)
        break