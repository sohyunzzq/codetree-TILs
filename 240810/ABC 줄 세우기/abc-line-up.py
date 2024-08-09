alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n = int(input())
lst = list(input().split())

cnt = 0
for i in range(n): #알파벳
    a = alpha[i]
    
    for j in range(n):
        if lst[j] == a:
            index = j
    
    for j in range(index - i):
        lst[index-j], lst[index-j-1] = lst[index-j-1], lst[index-j]
        cnt += 1

print(cnt)
'''
A B C D
D B A C i: 0, j: 2 / 1 2
D A B C i: 0,      / 0 1
A D B C

A B D C i: 1, j: 2 / 1 2

A B C D i: 2, j: 3 / 2 3
'''