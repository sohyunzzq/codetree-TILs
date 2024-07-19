def cal_sum(N):
    total = 0
    for i in range(1, N+1):
        total += i
    return int(total//10)

n = int(input())
print(cal_sum(n))