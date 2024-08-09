alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n, m, p = map(int, input().split())

lst = []
for i in range(m):
    lst.append(list(input().split()))

#p번째 메세지를 읽지 않은 사람 구해라
#내가 보내고 보낸 사람은 아님. 제외
#나 제외
#후보 중에, 내가 보내기 전에 보냈던 사람이랑 나랑 숫자 똑같으면 걔도 아님

read = [0] * n

for i in range(p-1, m): #나 + 내가 보내고 보낸 사람 1로 표시
    read[ord(lst[i][0]) - 65] = 1

for i in range(p-1): #내가 보내기 전에
    if int(lst[i][1]) == int(lst[p-1][1]):
        read[ord(lst[i][0]) - 65] = 1

for i in range(n):
    if read[i] == 0:
        print(alpha[i], end = " ")

'''
6 6 5
D 0
C 1
B 2
B 2
A 2
F 4

C 1
A B C D E F
x x x     x

B 2
A B C D E F
x x       x

A 2
A B C D E F
x         x
'''