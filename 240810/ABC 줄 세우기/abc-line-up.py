alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n = int(input())
lst = list(input().split())

cnt = 0
for i in range(n): #알파벳
    a = alpha[i]
    
    for j in range(n):
        if lst[j] == a:
            index = j #잘못된 자리에 있음
    
    for j in range(index - i):
        lst[index-j], lst[index-j-1] = lst[index-j-1], lst[index-j]
        cnt += 1

print(cnt)