a, b, c = map(int, input().split())

ans = 0
    
for i in range(c // a + 1):
    tmp = a * i #더 작은 수인 a를 i번 더하기
    
    #이제 목표는, tmp에 b를 더해서 c에 가까워지는 것
    #tmp에 최대 얼마만큼 b를 넣을 수 있는지, a로 계산했던 것처럼 계산
    #a는 0에 더하는 거였지만 여기는 이미 tmp가 존재하므로 계산 주의

    tmp += b * ((c - tmp) // b)
    ans = max(ans, tmp)

print(ans)