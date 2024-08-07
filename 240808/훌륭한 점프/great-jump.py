def jump(i):
    tmp = [0]
    for index, item in enumerate(lst):
        if item <= i:
            tmp.append(index)

    for i in range(len(tmp) - 1):
        if tmp[i+1] - tmp[i] > k:
            return False
    return True

n, k = map(int, input().split())
lst = list(map(int, input().split()))

#1번에서 시작해서 마지막에 도달해야 함
#최댓값이 최소가 되도록
#2 3 5 4 1

#5부터 내려가면서 답이라고 가정함
#5보다 작은 것들을 새로운 리스트에 담고, 그것들이 다 k 이내인지 검사

ans = n

for i in range(n, 0, -1): #i가 정답이라고 가정
    if jump(i):
        ans = min(ans, i)

print(ans)