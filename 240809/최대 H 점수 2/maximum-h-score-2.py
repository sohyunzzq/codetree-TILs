n, l = map(int, input().split())
lst = list(map(int, input().split()))

#수열에서 h 이상인 숫자가 h개 이상인가?를 찾아야 됨
#h개 이상이어야 하므로 될 수 있는 후보는 0 ~ n
#n개 중 l개는 1을 더해야 함
#h숫자가 0일 때부터 따져보기
#리스트를 정렬?
#100 3 2 1

lst.sort(reverse = True)

ans = 0
for i in range(1, n+1):
    cnt = 0
    down = l
    for j in range(n):
        if lst[j] >= i:
            cnt += 1
            continue
        if down == 0:
            break
        elif lst[j] + 1 >= i:
            cnt += 1
            down -= 1

    if cnt >= i:
        ans = i
        
print(ans)