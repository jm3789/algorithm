import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())

    # 스티커 정보 입력받기
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    stickers = [[0, 0]] + [[a[i], b[i]] for i in range(n)]

    # dp 리스트: 각 단계에서 해당 스티커로 끝났을 때 얻을 수 있는 최대 점수
    dp = [[0, 0] for _ in range(n+1)]
    dp[1][0] = stickers[1][0]
    dp[1][1] = stickers[1][1]

    # dp 점화식
    for i in range(2, n+1):
        dp[i][0] = stickers[i][0] + max(dp[i-2][1], dp[i-1][1])
        dp[i][1] = stickers[i][1] + max(dp[i-2][0], dp[i-1][0])

    # 결과 출력
    print(max(dp[n][0], dp[n][1]))