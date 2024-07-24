N, K, P, T = map(int, input().split())

inf = [0] * (N+1)
cnt = [0] * (N+1)

inf[P] = 1

lst = []
for i in range(T):
    lst.append(list(map(int, input().split())))
lst.sort(key = lambda x: x[0]) #t를 기준으로 정렬함

for i in range(T):
    if inf[lst[i][1]] == 1 and cnt[lst[i][1]] < K: #감염됐고 K번 미만 전염시킴
        inf[lst[i][2]] = 1
        cnt[lst[i][1]] += 1
    elif inf[lst[i][2]] == 1 and cnt[lst[i][2]] < K:
        inf[lst[i][1]] = 1
        cnt[lst[i][2]] += 1

for i in range(1, N+1):
    print(inf[i], end = "")