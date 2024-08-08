def findABCD():
    for a in range(15):
        for b in range(15):
            if a == b:
                continue
            for c in range(15):
                if a == c or b == c:
                    continue
                for d in range(15):
                    if a == d or b == d or c == d:
                        continue
                    A, B, C, D = lst[a], lst[b], lst[c], lst[d]
                    if A + B + C + D == maxi and A <= B <= C <= D:
                        check = [A, B, C, D, A+B, B+C, C+D, D+A, A+C, B+D, A+B+C, A+B+D, A+C+D, B+C+D, maxi]
                        if sorted(check) == sorted(lst):
                            print(A, B, C, D)
                            return

lst = list(map(int, input().split()))

#A+B+C+D는 무조건 제일 큰 값이 됨
#순회 돌면서 다 더했을 때 위 값이 나오는 거 4개 잡기
#A+B, B+C, ... 이 값들이 리스트에 있는지 확인

maxi = max(lst)
findABCD()