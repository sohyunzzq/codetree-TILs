k, n = map(int, input().split())

lst = []
for i in range(k):
    lst.append(list(map(int, input().split())))

#첫 번째 줄에서 모든 경우의 수를 찾기
#4번이 1번보다 항상 높은지 아랫줄 순회
#만약 4가 먼저 나오면 다음 줄, 1이 먼저 나오면 다음 조합
#그렇게 끝까지 다 찾았으면 카운트 증가

cnt = 0
for i in range(n):
    left = lst[0][i] #4, 1, 2, 3
    for j in range(i+1, n):
        check = True
        right = lst[0][j] #1, 2, 3 / 2, 3 / 3

        for m in range(1, k): #라인 순회
            for a in range(n):
                if lst[m][a] == left:
                    break
                elif lst[m][a] == right:
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