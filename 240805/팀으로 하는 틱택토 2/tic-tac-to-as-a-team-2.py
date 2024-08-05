lst = []
for i in range(3):
    lst.append(input())

#가로 세로 대각선
#경우마다 숫자가 두 종류가 있으면 됨
#배열에 1로 표시해서 합이 2면 됨

ans = 0
for i in range(3): #가로 순회
    check = [0] * 10
    for j in range(3):
        check[int(lst[i][j])] = 1
    if sum(check) == 2:
        ans += 1

for i in range(3): #세로 순회
    check = [0] * 10
    for j in range(3):
        check[int(lst[j][i])] = 1
    if sum(check) == 2:
        ans += 1

check = [0] * 10
for i in range(3):
    check[int(lst[i][i])] = 1
if sum(check) == 2:
    ans += 1

check = [0] * 10
for i in range(3):
    check[int(lst[2-i][i])] = 1
if sum(check) == 2:
    ans += 1

print(ans)