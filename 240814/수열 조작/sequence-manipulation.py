from collections import deque

dq = deque()
n = int(input())
for i in range(1, n+1):
    dq.append(i)

while len(dq) != 1:
    dq.popleft() #앞에서 하나 빼서 없애기
    dq.append(dq.popleft()) #앞에서 하나 뺀 다음 뒤로 넣기

print(dq.pop())