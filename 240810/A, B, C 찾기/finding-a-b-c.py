lst = list(map(int, input().split()))

#가장 큰 값(A+B+C)에서 제일 작은 값(A), 다음 작은 값(B)를 빼면 C
lst.sort()
c = lst[6] - lst[0] - lst[1]

print(lst[0], lst[1], c)