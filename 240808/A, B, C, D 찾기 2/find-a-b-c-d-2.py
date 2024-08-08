def findABCD():
    for a in range(15):
        for b in range(15):
            for c in range(15):
                for d in range(15):
                    A, B, C, D = lst[a], lst[b], lst[c], lst[d]
                    check = [A, B, C, D, A+B, B+C, C+D, D+A, A+C, B+D, 
                        A+B+C, A+B+D, A+C+D, B+C+D, A+B+C+D]
                    if sorted(check) == sorted(lst) and A <= B <= C <= D:
                        print(A, B, C, D)
                        return

lst = list(map(int, input().split()))

#순회 돌면서 다 더했을 때 위 값이 나오는 거 4개 잡기
#A+B, B+C, ... 이 값들이 리스트에 있는지 확인

findABCD()