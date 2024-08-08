n, k = map(int, input().split())

bomb = []
for i in range(n):
    bomb.append(int(input()))

#해당 번호가 몇 번 터졌는지 기록할 리스트 (크기가 이 정도는 괜찮은 듯)
#폭탄이 이미 터졌는지 기록할 리스트

numlst = [0] * (1000000 + 1) #번호를 체크
check = [0] * n #인덱스를 체크

for i in range(n):
    if check[i] == 1: #이미 터짐
        continue
    for j in range(i+1, n):
        if check[j] == 1: #이미 터짐
            continue
        if j > i + k: #범위 초과
            break
        
        if bomb[i] == bomb[j]:
            numlst[bomb[i]] += 1
            check[i], check[j] = 1, 1

maxi = 1
index = 0
for i in range(1000000 + 1):
    if numlst[i] >= maxi:
        maxi = numlst[i]
        index = i

print(index)