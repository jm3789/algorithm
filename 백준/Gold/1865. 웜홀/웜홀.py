import copy
import sys

input = sys.stdin.readline

TC = int(input())
for _ in range(TC):
    N, M, W = map(int, input().split())

    # 각 정점의 최단거리 정보
    d = [0 for _ in range(N + 1)]

    # 각 정점과 연결된 간선들 정보
    edges = [[] for _ in range(N + 1)]

    # 간선 정보 입력받기
    for _ in range(M):
        S, E, T = map(int, input().split())
        edges[S].append((E, T))
        edges[E].append((S, T))
    for _ in range(W):
        S, E, T = map(int, input().split())
        edges[S].append((E, -T))

    negative_flag = False
    tmp_d = []

    # 벨만포드 알고리즘
    for i in range(1, N+1):

        # 해당 노드들과 연결된 노드들의 최단거리 갱신
        for start_num in range(1, N+1):
            for edge in edges[start_num]:
                end_num = edge[0]
                weight = edge[1]
                if d[end_num] > d[start_num] + weight:
                    d[end_num] = d[start_num] + weight

        # N-1번째 반복이라면 d의 상태 저장: 리스트 깊은 복사
        if i == N-1:
            tmp_d = copy.deepcopy(d)

    # 음수 사이클이 존재하는지 여부
    negative_flag = d != tmp_d

    # 출력
    print('YES' if negative_flag else 'NO')