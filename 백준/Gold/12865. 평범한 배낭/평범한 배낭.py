N, K = map(int, (input().split()))

W = [0 for _ in range(N+1)]  # 무게
V = [0 for _ in range(N+1)]  # 가치
for i in range(1, N+1):
    W[i], V[i] = map(int, input().split())

# dp[i][j]: i번째 물건까지 고려하고, j무게까지 담을 수 있을 때 최대 가치
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]  

# w v
#       0kg 1kg 2kg 3kg 4kg 5kg 6kg 7kg
# 0 0    0   0   0   0   0   0   0   0
# 6 13   0   0   0   0   0   0   13  13
# 4 8    0   0   0   0   8   8   13  13
# 3 6    0   0   0   6   8   8   13  14
# 5 12   0   0   0   6   8   12  13  14

for i in range(1, N+1):
    for j in range(1, K+1):
        # 점화식: max(dp[i-1][j] , dp[i-1][j-W[i]] + V[i]])
        if j >= W[i]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-W[i]] + V[i])
        else:
            dp[i][j] = dp[i-1][j]

# print(dp)
print(dp[N][K])
