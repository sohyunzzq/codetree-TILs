a, b, c = map(int, input().split())

#맨 끝 사람이 나머지 사이로
#2 6 9
#6 8 9
#6 7 8

#2 6 9
#6 7 9
#7 8 9

#1 7 12
#7 9 12

#더 먼 사람을 가까이 오게 하기
#그런데 나머지 두 수가 연속되면 올 수 없음
#가까이 부를 때 2만큼

if (a + 1 == b and b + 1 == c) or (a - 1 == b and b - 1 == c):
    print(0)
elif (a + 2 == b) or (b + 2 == c) or (a - 2 == b) or (b - 2 == c):
    print(1)
else:
    print(2)