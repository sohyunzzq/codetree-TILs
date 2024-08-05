n = int(input())
alpha = input()

#ABCDABC
#시작점을 먼저 잡아주고 (A~, B~, C~, ...)
#끝점을 잡아주기 (A, ~B, ~C)
#그렇게 문자열을 새로 만들어준 후, 처음부터 순회하면서 있는지 세기
#길이가 1인 문자열 두 번 이상 나오는 거 있고, 2도 두 번 이상 나오는 게 있음
check = [0] * 101

ans = 100
for i in range(n):
    for j in range(1, n+1):
        if i < j:
            temp = alpha[i:j]

        cnt = 0
        for k in range(n-len(temp)+1):
            if alpha[k:k+len(temp)] == temp:
                cnt += 1
                if cnt >= 2:
                    check[len(temp)] = 1
                    break
        
        if cnt == 1 and check[len(temp)] != 1:
            ans = min(ans, len(temp)) 
                
print(ans)