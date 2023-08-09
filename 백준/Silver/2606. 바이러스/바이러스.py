import sys

N = int(sys.stdin.readline())

# 각 컴퓨터에 연결되어 있는 컴퓨터들의 번호를 리스트들로 저장
network_list = [[] for _ in range(N)]
network_list.insert(0, 0)
it = int(sys.stdin.readline())
for _ in range(it):
    a, b = map(int, sys.stdin.readline().split())
    if b not in network_list[a]:
        network_list[a].append(b)
    if a not in network_list[b]:
        network_list[b].append(a)
# 예제에서 network_list는 [0, [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]].

# virus_list: 각 컴퓨터들이 바이러스에 걸렸는지 여부
virus_list = [False for _ in range(N)]
virus_list.insert(0, 0)
virus_list[1] = True


# origin_num 컴퓨터에서 인접한 컴퓨터들을 감염시키는 함수
def infect(origin_num):
    for infected_num in network_list[origin_num]:
        if virus_list[infected_num] != True:
            virus_list[infected_num] = True 
            infect(infected_num)  # 재귀적으로 다음 컴퓨터를 감염시킴

# 1번 컴퓨터에서 바이러스 전파 시작
infect(1) 

# 출력
print(virus_list[2:].count(True))