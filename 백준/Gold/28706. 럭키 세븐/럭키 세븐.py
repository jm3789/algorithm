# 만들 수 있는 수를 모두 저장하는 것이 아닌, 만들 수 있는 수를 7로 나눈 나머지만 저장하기
# DP: 중복 계산 제거

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())  # N: 줄의 수

    # dp[i][remain]: i번째 줄의 계산까지 마쳤을 때, 나머지가 remain이 되는 게 가능한지 여부
    dp = [[False for _ in range(7)] for _ in range(N+1)]
    dp[0][1] = True  # 1에서 시작
    
    def calculate(remain, op, v):
        if op == '+':
            return (remain + v) % 7
        elif op == '*':
            return (remain * v) % 7

    for i in range(1, N+1):
        op1, v1, op2, v2 = sys.stdin.readline().split()
        for remain in range(7):
            if dp[i-1][remain] == True: # i번째 줄의 계산까지 마쳤을 때, 나머지가 remain이 되는 게 가능함
                dp[i][calculate(remain, op1, int(v1))] = True
                dp[i][calculate(remain, op2, int(v2))] = True
    
    if dp[N][0] == True:  # 마지막 턴에서 나머지가 0이 되는 게 가능한지 체크
        print('LUCKY')
    else:
        print('UNLUCKY')
