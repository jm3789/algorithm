import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())

    # 스티커 정보 입력받기
    a = [0] + list(map(int, input().split()))
    b = [0] + list(map(int, input().split()))
    stickers = [a, b]

    # dp 리스트: 각 단계에서 해당 스티커로 끝났을 때 얻을 수 있는 최대 점수
    dp = [[0 for _ in range(n+1)] for _ in range(2)]
    dp[0][1] = stickers[0][1]
    dp[1][1] = stickers[1][1]

    # dp 점화식
    for i in range(2, n+1):
        dp[0][i] = max(dp[1][i-2], dp[1][i-1]) + stickers[0][i]
        dp[1][i] = max(dp[0][i-2], dp[0][i-1]) + stickers[1][i]

    # 결과 출력
    print(max(dp[0][n], dp[1][n]))