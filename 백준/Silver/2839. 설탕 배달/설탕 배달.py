# Dynamic Programming으로 풀어보기

N = int(input())

dp = [5555 for _ in range(N+5)]  # dp 배열 생성

# dp[1] = 5555
# dp[2] = 5555
dp[3] = 1
# dp[4] = 5555
dp[5] = 1

for i in range(6, N+1):
    dp[i] = min(dp[i-3], dp[i-5]) + 1  # 점화식
# dp[6] = min(dp[3], dp[1]) + 1 = min(1, 5555) + 1 = 2
# dp[7] = min(dp[4], dp[2]) + 1 = min(5555, 5555) + 1 = 5556
# dp[8] = min(dp[5], dp[3]) + 1 = min(1, 1) + 1 = 2
# ...

if dp[N] >= 5555:  # 정확히 N킬로그램을 만들 수 없을 때, dp[N]은 5555이거나 5556임.
    print(-1)
else:
    print(dp[N])
