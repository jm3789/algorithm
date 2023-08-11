# 파이썬의 기본 재귀 limit: 1000. 변경하지 않으면 RecursionError

import sys
sys.setrecursionlimit(5000)  # 재귀 limit 변경

# 입력
T = int(sys.stdin.readline())
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())

    # 배추가 심어져 있는 좌표 정보 입력받아 리스트에 저장
    cabbage_list = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        cabbage_list[Y][X] = 1

    # cabbage_list[y][x] == 1인 경우 실행되는 함수
    def protect(x, y): 
        # 해당 좌표의 1을 0으로 바꿈
        cabbage_list[y][x] = 0
        # 상하좌우를 재귀적으로 확인하여 인접해있는 모든 1을 0으로 바꿈
        # 상
        if y != 0:
            if cabbage_list[y-1][x] == 1:
                protect(x, y-1)
        # 하
        if y != N-1:
            if cabbage_list[y+1][x] == 1:
                protect(x, y+1)
        # 좌
        if x != 0:
            if cabbage_list[y][x-1] == 1:
                protect(x-1, y)
        # 우
        if x != M-1:
            if cabbage_list[y][x+1] == 1:
                protect(x+1, y)

    # 필요한 지렁이 마리 수 구하기
    worm = 0
    for x in range(M):
        for y in range(N):
            if cabbage_list[y][x] == 1:  # 배추가 있으면
                protect(x, y)
                worm += 1  # 지렁이가 필요함

    # 출력
    print(worm)
        