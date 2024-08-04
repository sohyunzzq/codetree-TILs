k, n = map(int, input().split())

lst = []
for i in range(k):
    lst.append("".join(input().split()))

#첫 번째 줄에서 모든 경우의 수를 찾기
#4번이 1번보다 항상 높은지 아랫줄 순회
#find를 써서, 결과값이 항상 > 이어야 함
#만약 < 이 나오면 다음 경우의 수를 찾으러 감
#그렇게 끝까지 다 찾았으면 카운트 증가

cnt = 0
for i in range(n):
    left = lst[0][i] #4, 1, 2, 3
    for j in range(i+1, n):
        check = True
        right = lst[0][j] #1, 2, 3 / 2, 3 / 3

        for m in range(1, k):
            if lst[m].find(left) > lst[m].find(right):
                check = False
                break
        if check:
            cnt += 1

print(cnt)
        

'''
4 1 2 3
4 1 3 2
4 2 1 3
'''