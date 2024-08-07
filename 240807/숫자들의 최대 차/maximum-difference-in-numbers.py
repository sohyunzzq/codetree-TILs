n, k = map(int, input().split())

lst = []
for i in range(n):
    lst.append(int(input()))

#정렬을 하고, 최소 고정해놓고 최대에서 하나씩 줄여가면서 차이 넘는지 체크하기
#1 1 3 4 6
#1 1 3 4 6 7 8 11 15 일 때 개수 세는 법
#3부터 11까지 센다 → 6개임
#인덱스 2, 7이므로 j - i + 1

lst.sort()

ans = 0
for i in range(n): #최솟값 고정
    min_val = lst[i]
    for j in range(n-1, i, -1): #뒤에서부터 고정해둔 최솟값까지 접근
        max_val = lst[j]
        if max_val > min_val + k:
            continue
        ans = max(ans, j - i + 1)

print(ans)