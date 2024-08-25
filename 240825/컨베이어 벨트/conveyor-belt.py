def shift(lst, tmp):
    for i in range(len(lst)-1, 0, -1):
        lst[i] = lst[i-1]
    lst[0] = tmp

n, t = map(int, input().split())

lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
t %= (2 * n)

for i in range(t):
    first = lst1[::-1][0]
    second = lst2[::-1][0]

    shift(lst1, second)
    shift(lst2, first)

for item in lst1:
    print(item, end = " ")
print()
for item in lst2:
    print(item, end = " ")


'''
1 2 3 4 5
6 5 1 7 8

첫 번째 줄 맨 마지막 원소를 저장: first
두 번째 줄 맨 마지막 원소를 저장: second

첫 번째 줄 맨 앞에 second 넣고 뒤로 밀기
두 번째 줄 맨 앞에 first 넣고 뒤로 밀기
'''