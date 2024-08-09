alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n = int(input())
lst = list(input().split())

cnt = 0
for i in range(n): #알파벳
    for j in range(n): #리스트에 저장된 문자
        if alpha[i] == lst[j]:
            for k in range(j-i, 0, -1):
                lst[k+i], lst[k+i-1] = lst[k+i-1], lst[k+i]
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