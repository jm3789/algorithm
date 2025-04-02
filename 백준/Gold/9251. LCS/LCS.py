s1 = input()
s2 = input()

# dp[i][j]: str1의 i번째 문자까지와 str2의 j번째 문자까지의 LCS 길이
# s1[i-1] == s2[j-1]이면 dp[i][j] = dp[i-1][j-1] + 1
# s1[i-1] != s2[j-1]이면 dp[i][j] = max(dp[i-1][j], dp[i][j-1])
# 시간 복잡도: O(NM)

dp = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]

for i in range(1, len(s1)+1):
    for j in range(1, len(s2)+1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len(s1)][len(s2)])