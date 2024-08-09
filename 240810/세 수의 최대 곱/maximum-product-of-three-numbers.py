n = int(input())
lst = list(map(int, input().split()))

#3개의 숫자 곱하기
#결과 양수: 양양양, 양음음
#결과 음수: 양양음, 음음음 (0이 있으면 0이 최대, 없으면 절댓값 작은 숫자)

#양이 3개 이상: 양양양 / 양이 1개 이상 & 음이 2개 이상: 양음음 비교

plus = []
minus = []
zero = False

for num in lst:
    if num > 0:
        plus.append(num)
    elif num < 0:
        minus.append(num)
    else:
        zero = True

ans = lst[0] * lst[1] * lst[2]

if len(plus) >= 1: #결과 양수
    plus.sort(reverse = True) # 3 2 1
    minus.sort()              # -3 -2 -1

    if len(plus) >= 3:
        ans = plus[0] * plus[1] * plus[2]
    if len(minus) >= 2:
        ans = max(ans, plus[0] * minus[0] * minus[1])

else: #결과 음수
    if zero == True:
        ans = 0
    else:
        plus.sort()                 # 1 2 3
        minus.sort(reverse = True)  # -1 -2 -3

        if len(minus) >= 3:
            ans = minus[0] * minus[1] * minus[2]
        if len(plus) >= 2:
            ans = max(ans, minus[0] * plus[1] * plus[2])

print(ans)