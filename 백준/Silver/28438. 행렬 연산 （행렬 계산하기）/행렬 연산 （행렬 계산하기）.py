import sys

# 입력
N, M, Q = map(int, sys.stdin.readline().split())

# 각 행과 열에 더해질 값을 기록할 리스트
row_list = [0 for _ in range(N)] 
col_list = [0 for _ in range(M)]

# 입력받고 계산
for _ in range(Q):
    axis, idx, v = map(int, sys.stdin.readline().split())
    # 더해질 값에 v만큼 누적
    if axis == 1:
        row_list[idx-1] += v  
    else:
        col_list[idx-1] += v

# 출력
for i in range(N):
    for j in range(M):
        print(row_list[i] + col_list[j], end=' ')  # i번째 행에 더해질 값 + j번째 열에 더해질 값
    print()