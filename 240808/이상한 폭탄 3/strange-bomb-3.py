n, k = map(int, input().split())

bomb = []
for i in range(n):
    bomb.append(int(input()))

#검사한 번호는 리스트에 넣어서 다시 검사하지 않게
#b 기준 앞뒤 k 이내에 같은 수가 있는지 세서 있으면 1 더함
#범위 넘치는 거 주의하기
#ans와 num을 이용해서 폭탄 번호도 기억하기

check = []
ans = 0
maxi = 1
for i in range(n):
    b = bomb[i]
    if b in check: #이미 검사한 숫자
        continue

    cnt = 0
    for j in range(n):
        if bomb[j] == b:
            for m in range(j-k, j+k+1):
                if 0 <= m < n and bomb[m] == b and j != m:
                    cnt += 1

    if cnt > maxi:
        maxi = cnt
        ans = b
    elif cnt == maxi:
        ans = max(ans, b)
    
    check.append(b)

print(ans)