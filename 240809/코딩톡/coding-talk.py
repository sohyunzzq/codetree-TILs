def talk():
    if int(lst[p-1][1]) == 0: #다 읽으면 아무것도 출력 X
        return

    read = [0] * n #읽었으면 1

    for i in range(p-1, m): #나랑 나 다음 보낸 사람들은 제외
        read[ord(lst[i][0]) - 65] = 1
    
    for i in range(p-1):
        if int(lst[i][1]) == int(lst[p-1][1]): #B 2 A 2 인 경우, B는 읽은 거
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