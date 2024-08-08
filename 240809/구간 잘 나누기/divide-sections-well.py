n, m = map(int, input().split())
lst = list(map(int, input().split()))

# 잘 생각해 보면, 구간의 합의 최댓값을 결정한다면
# 구간을 몇 개로 나눠야 하는지 손쉽게 찾을 수 있습니다.

for i in range(max(lst), 100*100 + 1):
    # 구간의 합의 최댓값이 i일 때

    # check: 구간을 나눌 수 있으면 true
    # section: 나뉘어져야 하는 구간의 개수
    section = 1

    sum1 = 0
    for j in range(n):
        if sum1 + lst[j] > i: #이 다음부터 다음 구간
            sum1 = 0
            section += 1

        sum1 += lst[j]

    if section <= m:
        print(i)
        break