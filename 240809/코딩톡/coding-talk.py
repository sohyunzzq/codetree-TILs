def talk():
    if int(lst[p-1][1]) == 0: #다 읽으면 아무것도 출력 X
        return

    read = [0] * n
    for i in range(p-1, m):
        read[ord(lst[i][0]) - 65] = 1
    
    for i in range(p-1):
        if int(lst[i][1]) == int(lst[p-1][1]):
            read[ord(lst[i][0]) - 65] = 1
    
    for i in range(n):
        if read[i] == 0:
            print(alpha[i], end = " ")

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n, m, p = map(int, input().split())

lst = []
for i in range(m):
    lst.append(list(input().split()))

talk()

'''
내 위로 보낸 사람, 나 제외
0이면 걍 바로 끝
후보 중에서, 내가 보내기 전에 보냈고, 나랑 숫자 똑같으면 제외

D 0:                [E]
C 1: D E            [D E]
B 2: C D E          [C D E]
B 2: C D E         
A 2: C D E          [B C D E] 
F 4: A B C D E      [A B C D E]
'''