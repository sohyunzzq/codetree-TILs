lst = []
for i in range(3):
    lst.append(input())

#가로 세로 대각선
#경우마다 숫자가 두 종류가 있으면 됨
#배열에 1로 표시해서 합이 2면 됨
#그런데 111 555 111 의 경우, 1번과 5번이 팀을 하는 경우는 하나이므로 답은 1임
#경우의 수를 따로 저장해두어야 함

team = []
ans = 0
for i in range(3): #가로 순회
    check = [0] * 10
    for j in range(3):
        check[int(lst[i][j])] = 1

    if sum(check) == 2:
        temp = []
        for j in range(10):
            if check[j] != 0:
                temp.append(j)
        if temp not in team:
            ans += 1
            team.append(temp)

for i in range(3): #세로 순회
    check = [0] * 10
    for j in range(3):
        check[int(lst[j][i])] = 1

    if sum(check) == 2:
        temp = []
        for j in range(10):
            if check[j] != 0:
                temp.append(j)
        if temp not in team:
            ans += 1
            team.append(temp)

check = [0] * 10
for i in range(3):
    check[int(lst[i][i])] = 1

if sum(check) == 2:
    temp = []
    for j in range(10):
        if check[j] != 0:
            temp.append(j)
    if temp not in team:
        ans += 1
        team.append(temp)

check = [0] * 10
for i in range(3):
    check[int(lst[2-i][i])] = 1

if sum(check) == 2:
    temp = []
    for j in range(10):
        if check[j] != 0:
            temp.append(j)
    if temp not in team:
        ans += 1
        team.append(temp)

print(ans)