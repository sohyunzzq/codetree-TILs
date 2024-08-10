n = int(input())
lst = list(map(int, input().split()))

#뒤에서부터 검사하면서 오름차가 되게 끼우기

ans = 0
while True:
    if lst == sorted(lst):
        print(ans)
        break
    
    ans += 1
    num = lst[0]

    #첫 번째 원소 뺀 리스트
    lst2 = []
    for i in range(1, n):
        lst2.append(lst[i])

    #어디서부터 오름차로 진행되는지
    for i in range(n-1-1, -1, -1):
        if lst2[i] < lst2[i-1]:
            index = i
            break
    
    #index부터 n-1 까지는 오름차임
    #[0, index)까지 리스트에 그대로 담고,
    #index부터 나머지를 넣을 건데
    #이때 num이 낄 수 있을 때 끼기

    lst = []
    for i in range(index):
        lst.append(lst2[i])

    for i in range(index, n-1):
        if num < lst2[i]:
            lst.append(num)
            num = n+1 #다시 검사하지 않도록
        lst.append(lst2[i])
    if num != n + 1:
        lst.append(num)
    
#2 4 8 3 1 6 7 5

#4 8 9 1 6 7 3 5 / 2