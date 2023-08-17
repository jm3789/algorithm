# DP: bottom-up 방식으로 풀어보기

import sys

N = int(sys.stdin.readline())

stair_list = []  # 계단에 쓰여 있는 점수 리스트
for _ in range(N):
    stair_list.append(int(sys.stdin.readline()))

# 각 계단이 도착점일 때의 최대 점수를 리스트로 저장.
# (이전 계단을 밟고 도착할 때 가능한 최대 점수, 이전 계단을 건너뛰고 도착할 때 가능한 최대 점수)의 형태로 저장
dp = [(stair_list[0], 0)]
if N > 1:
    dp.append((stair_list[1], stair_list[0] + stair_list[1]))  
    for i in range(2, N):
        dp.append((max(dp[i-2]) + stair_list[i], dp[i-1][0] + stair_list[i]))  # 점화식

print(max(dp[N-1]))