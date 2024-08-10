n, m = map(int, input().split())
lst = list(map(int, input().split()))

#거리가 m 이내에 있으면 사용 가능
#처음 1이 나오면, m칸 더 가서 거기에 설치
#00110011100111110
#   -   -    -  -  와이파이 설치한 곳
#  === ===  ====== 와이파이 가능한 곳 [i, i+2*m]

ans = 0
i = 0
while True:
    if i >= n:
        break

    if lst[i] == 1:
        ans += 1
        i += 2 * m
    i += 1
print(ans)