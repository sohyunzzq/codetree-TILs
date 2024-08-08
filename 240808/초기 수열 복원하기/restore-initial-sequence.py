def check(i):
    tmp = [i]
    for j in range(n-1):
        num = lst[j] - tmp[j]
        if num in tmp or num > n:
            return False
        tmp.append(num)
    return tmp


n = int(input())
lst = list(map(int, input().split()))

#첫 원소를 잡고,
#리스트의 0번 인덱스값에서 tmp의 0번 인덱스값을 뺀 후 tmp에 추가
#이때, 만약 tmp에 그 값이 이미 있거나 n을 초과하면 첫 원소를 바꿈

ans = []
for i in range(1, n + 1): #첫 원소
    if check(i):
        ans.append(check(i))
ans.sort()

for i in range(n):
    print(ans[0][i], end = " ")