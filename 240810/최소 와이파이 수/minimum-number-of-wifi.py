n, m = map(int, input().split())
lst = list(map(int, input().split()))

#거리가 m 이내에 있으면 사용 가능
#처음 1이 나오면, m칸 더 가서 거기에 설치
#00110011100111110
#   -   -    -  -  와이파이 설치한 곳
#  === ===  ====== 와이파이 가능한 곳 [i, i+2*m]

#110111
#===

wifi = [0] * n
ans = 0
for i in range(n):
    if lst[i] == 1 and wifi[i] == 0:
        ans += 1
        for j in range(i, i+2*m + 1):
            if 0 <= j < n:
                wifi[j] = 1
print(ans)