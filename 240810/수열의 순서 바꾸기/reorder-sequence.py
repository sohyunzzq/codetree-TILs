n = int(input())
lst = list(map(int, input().split()))

#뒤에서부터 검사하면서,
#정렬 안 돼 있는 건 옮겨야 한단 뜻

#8 7 6 5 4 3 2 1

index = n - 1
while True:
    if lst[index] < lst[index - 1]:
        break
    index -= 1
print(index)