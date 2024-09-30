n = int(input())

dp = [0] * (n + 1)
dp[0] = 1
dp[1] = 0
dp[2] = 1
dp[3] = 1

for i in range(4, n + 1):
    dp[i] = dp[i-2] + dp[i-3]

print(dp[n] % 10007)