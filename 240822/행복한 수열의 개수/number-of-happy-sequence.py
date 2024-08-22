def check(seq):
    cnt = 1
    max_cnt = 1
    for i in range(1, n):
        if seq[i-1] == seq[i]:
            cnt += 1
        else:
            cnt = 1
        
        max_cnt = max(max_cnt, cnt)
    
    if max_cnt >= m:
        return True
    return False

n, m = map(int, input().split())
lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))

ans = 0


#가로를 체크
for i in range(n):
    if check(lst[i]):
        ans += 1

#세로를 체크
for j in range(n):
    tmp = []
    for i in range(n):
        tmp.append(lst[i][j])
    if check(tmp):
        ans += 1

print(ans)