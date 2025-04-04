s1 = input()
s2 = input()

dp = [0 for _ in range(len(s2)+1)]
dp_lcs = ['' for _ in range(len(s2)+1)]

for i in range(1, len(s1)+1):
    # prev: 대각선(left-top) 값
    prev = 0  # 이전 대각선(dp[j-1])의 LCS 길이
    prev_lcs = ''

    for j in range(1, len(s2)+1):
        # tmp: 현재 dp[j] 값을 백업
        tmp = dp[j]
        tmp_lcs = dp_lcs[j]

        if s1[i-1] == s2[j-1]:
            dp[j] = prev + 1
            dp_lcs[j] = prev_lcs + s1[i-1]
        else:
            if dp[j-1] > dp[j]:
                dp[j] = dp[j-1]
                dp_lcs[j] = dp_lcs[j-1]

        # prev를 현재 dp[j] 값으로 업데이트: 다음 열에서 사용
        prev = tmp
        prev_lcs = tmp_lcs

print(dp[len(s2)])
if dp[len(s2)] > 0:
    print(dp_lcs[len(s2)]) 