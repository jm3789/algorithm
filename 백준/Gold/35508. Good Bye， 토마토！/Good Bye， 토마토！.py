import sys
input = sys.stdin.readline
from bisect import bisect_right

N, D = map(int, input().split())

foods = []
for _ in range(N):
    T, A, B = map(int, input().split())
    foods.append((T, A, B))
foods.sort()

T_list = [food[0] for food in foods]
A_list = [food[1] for food in foods]
B_list = [food[2] for food in foods]

# B의 최댓값 기억하는 리스트 만들기
prefix_max_B = [0] * N
prefix_max_B[0] = B_list[0]
for i in range(1, N):
    prefix_max_B[i] = max(prefix_max_B[i-1], B_list[i])

# T는 정렬되어있고, 같은 인덱스에 해당 시간일 경우 B 심사위원에게 얻을 수 있는 최대점수가 들어가게 됨

answer = 0
for i in range(N):
    T = T_list[i]
    A = A_list[i]
    B = B_list[i]

    answer_1, answer_2 = 0, 0

    # i번째 요리 하나만 사용하는 경우
    if T <= D:
        answer_1 = A + B

    # i번째 요리로 A 심사위원의 점수를 따고, 남은 시간동안 B의 최대 점수를 따는 경우
    remain = D - T
    if remain <= 0:
        answer_2 = A
    else:
        index = bisect_right(T_list, remain) - 1
        if index >= 0:
            answer_2 = A + prefix_max_B[index]
        else:
            answer_2 = A
    answer = max(answer, answer_1, answer_2)

print(answer)