# 세로로 앱 정보: (바이트, 비용)
# 가로로 비용

# i : 앱 번호
# dp[j] = j비용으로 확보할 수 있는 최대 바이트
N, M = map(int, input().split())
A = [0] + list(map(int, input().split()))  # 바이트 수
C = [0] + list(map(int, input().split()))  # 비용

dp = [0 for _ in range(sum(C) + 1)]

# 점화식
# dp[j] = max(dp[j], dp[j - C[i]] + A[i])
for i in range(1, N+1):
    for j in range(sum(C), -1, -1): # 뒤에서부터 갱신
        # 이 앱의 비용이 j비용보다 작거나 같을 때에만 이 앱을 고려할 수 있음
        if j >= C[i]:
            dp[j] = max(dp[j], dp[j - C[i]] + A[i])
    # print(dp)

# 처음으로 M바이트 이상 확보할 수 있는 지점을 출력
for i in range(sum(C) + 1):
    if dp[i] >= M:
        print(i)
        break