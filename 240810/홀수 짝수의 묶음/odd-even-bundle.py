n = int(input())
lst = list(map(int, input().split()))

even = 0
odd = n
for num in lst:
    if num % 2 == 0:
        even += 1
        odd -= 1

#최대한 많이 나누려면
#합이 홀수: 홀 1개
#합이 짝수: 짝 1개, 없으면 홀 2개

#묶음이 짝수 개째면 총합을 짝수로 만들고, 홀수 개째면 총합을 홀수로 만들기
#1
group = 0
while True:
    if group % 2 == 0: #짝수 만들기
        if even:
            even -= 1
            group += 1
        elif odd >= 2:
            odd -= 2
            group += 1
        elif odd == 1: #짝수 없음, 홀수 1개 남음.
                       #어딜 껴도 문제가 일어남
                       #따라서, 직전에 만든 홀수 묶음을 풀어서 홀수 하나 꺼내고,
                       #그 전에 있는 짝수 묶음에 다 되어버리기
            group -= 1
            break
        else: #숫자 다 씀. 걍 끝내면 됨
            break

    else: #홀수 만들기
        if odd:
            odd -= 1
            group += 1
        else: #홀수 없음. 짝수가 남아 있어도 아무데나 끼면 됨
            break
print(group)