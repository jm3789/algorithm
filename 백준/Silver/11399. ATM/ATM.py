# 시간이 적게 걸리는 사람부터 돈을 인출

import sys
N = int(sys.stdin.readline())

time_list = sorted(list(map(int, sys.stdin.readline().split())))  # 각 사람의 돈 인출 시간
total_time = 0  # 필요한 시간의 합

for i in range(N):  # 첫번째 사람부터 순서대로 실행

    # waiting_time: 현재 사람에게 필요한 시간
    waiting_time = 0  

    # 앞선 사람들부터 해당 번째 사람까지의 돈 인출 시간을 모두 더함
    j = 0
    while j <= i:
        waiting_time += time_list[j] 
        j += 1 

    # total_time에 더해줌
    total_time += waiting_time  

print(total_time)  # 출력