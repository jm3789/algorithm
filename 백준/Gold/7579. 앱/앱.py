# 세로로 앱 정보: (바이트, 비용)
# 가로로 바이트 수

# i : 앱 번호
# dp[j] = j비트를 확보했을 때의 최소 비용
N, M = map(int, input().split())
A = [0] + list(map(int, input().split()))  # 바이트 수
C = [0] + list(map(int, input().split()))  # 비용
dp = [sum(C) + 1 for _ in range(M+1)]

# 점화식
# dp[j] = min(dp[j], dp[j - A[i]] + C[i])
for i in range(1, N+1):
    for j in range(M, -1, -1): # 뒤에서부터 갱신
        if A[i] >= j:
            # A[i] : i번째 앱의 바이트 수가 현재 확보해야 하는 바이트 수보다 크거나 같다면
            dp[j] = min(dp[j], C[i])
        else:
            dp[j] = min(dp[j], dp[j - A[i]] + C[i])
    # print(dp)
print(dp[M])