# dp
# 최댓값 구하는 dp랑 최솟값 구하는 dp를 전체로 각각 관리하면 메모리초과

# 1 2 3
# 6 3 1
# 0 4 9

N = int(input())
dp1_a = dp1_b = dp1_c = 0
dp2_a = dp2_b = dp2_c = 0

for _ in range(N):
    now1, now2, now3 = map(int, input().split())

    a = max(dp1_a, dp1_b) + now1
    b = max(dp1_a, dp1_b, dp1_c) + now2
    c = max(dp1_b, dp1_c) + now3
    dp1_a = a
    dp1_b = b
    dp1_c = c

    a = min(dp2_a, dp2_b) + now1
    b = min(dp2_a, dp2_b, dp2_c) + now2
    c = min(dp2_b, dp2_c) + now3
    dp2_a = a
    dp2_b = b
    dp2_c = c

print(max(dp1_a, dp1_b, dp1_c), min(dp2_a, dp2_b, dp2_c))