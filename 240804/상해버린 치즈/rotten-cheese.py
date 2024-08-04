n, m, a, b = map(int, input().split())

ate = []
for i in range(a): #사람, 치즈, 언제
    ate.append(list(map(int, input().split())))

sick = {}
for i in range(b): #사람, 언제
    p, t = map(int, input().split())
    sick[p] = t

ate.sort(key = lambda x: (x[1], x[0], x[2]))

#1번 사람이 3초부터 아팠다면, 3초 이후에 먹은 치즈는 절대 상한 게 아님
#1번으로 인해 1, 2, 4 중 하나인데 2번은 4번을 안 먹고도 아팠음 이걸 어떻게 알아낼지
#치즈를 돌리면서 순회를 할까?
#1번 치즈 - 1번이 아프기 전 먹음, 2번이 아프기 전 먹음 -> 후보에 올리기

cheese = [0] * (m+1)

for i in range(1, m+1):
    check = [0] * (n+1)
    for j in range(a):
        if ate[j][1] == i and ate[j][0] in sick and ate[j][2] < sick[ate[j][0]]:
            check[ate[j][0]] = 1
    if sum(check) == b:
        cheese[i] = 1

answer = 0
for i in range(1, m+1):
    if cheese[i] == 1:
        for j in range(a):
            if ate[j][1] == i:
                check[ate[j][0]] = 1
        answer = max(answer, sum(check))

print(answer)

'''
1 1 1
2 1 5
3 1 3
1 2 2
2 2 7
1 3 4
1 4 1
'''