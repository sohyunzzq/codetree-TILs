alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n, m, p = map(int, input().split())

lst = []
for i in range(m):
    lst.append(list(input().split()))

#p번째 메세지를 읽지 않은 사람 구해라
#lst[p-1]번째 메세지를 확실하게 읽은 사람을 빼기
#p-1부터 m까지 나온 알파벳들은 확실하게 읽음
#참가자는 alpha[0] ~ alpha[n-1]

read = [0] * n #읽으면 1로 표시

for i in range(p-1, m):
    read[ord(lst[i][0])-65] = 1

for i in range(n):
    if read[i] == 0:
        print(alpha[i], end = " ")