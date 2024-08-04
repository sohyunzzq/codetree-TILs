n, m, d, s = map(int, input().split())

ate = []
for i in range(d): #몇 번째 사람(p)이 몇 번째 치즈(m)를 언제(t초)
    ate.append(list(map(int, input().split())))

sick = []
for i in range(s): #몇 번째 사람(p)이 언제(t초) 아팠는지
    sick.append(list(map(int, input().split())))

#1번 사람이 3초에 아팠으면 3초부터 먹은 치즈들은 후보가 아님
#치즈 리스트에서 1번 사람이 3초 전에 먹은 것은 다 1을 더함
#다 돌고 치즈 리스트값이 s값과 같으면 그게 최종
#치즈를 m개 먹고 무조건 치즈 번호는 연속됨

cheese = [0] * (m+1)

#같은 치즈를 2번 이상 먹을 수도 있음
#다른 치즈일 때만 카운트를 올려주기 위해 정렬 후 진행

ate.sort(key = lambda x: (x[0], x[1]))
for i in range(s):
    p = sick[i][0]
    time = sick[i][1]

    for j in range(d):
        if p == ate[j][0] and (j == 0 or ate[j][1] != ate[j-1][1]) and ate[j][2] < time:
            cheese[ate[j][1]] += 1 #상한 치즈 가능성

#최종 치즈 리스트를 바깥 포문
#ate 리스트를 돌며 먹은 카운트 세고 최댓값 구하기

max_val = 0
answer = [0] * (n+1)
for i in range(1, m+1):
    if cheese[i] == s: #i번 치즈를 먹은 사람 세기
        cnt = 0
        for j in range(d):
            if ate[j][1] == i:
                answer[ate[j][0]] = 1
                
        max_val = max(max_val, sum(answer))

print(max_val)