import copy
import heapq
import sys
input = sys.stdin.readline

# 방문하는 도시도 출력하기

N = int(input())
M = int(input())

edges = [[] for _ in range(N+1)]

for _ in range(M):
    start, end, weight = map(int, input().split())
    edges[start].append((end, weight))  # (도착 노드번호, 비용)

S, E = map(int, input().split())

# TODO: deepcopy는 쓰지 않아도 된다! 이전 노드를 딱 하나만 기억해도 전체 경로를 역추적할 수 있기 때문. prev로 이전노드 저장하자
d = [float('inf') for _ in range(N+1)]  # 최단거리 리스트
d[0] = 0
d[S] = 0
path = [[] for _ in range(N+1)]  # 방문한 노드 번호들 2차원 리스트

pq = []
pq.append((0, S))  # (현재 최단거리, 출발 노드번호)

while pq:
    # 노드 pop
    dist, start = heapq.heappop(pq)  # dist는 이 노드가 pq로 들어가던 시점에서의 최단거리
    # 이미 다른 더 작은 값으로 갱신되었다면 패스
    if d[start] < dist:
        continue

    # 해당 노드 확인
    for end, weight in edges[start]:

        # 최단거리 갱신하면서 pq에 넣기
        if d[start] + weight < d[end]:
            d[end] = d[start] + weight
            path[end] = copy.deepcopy(path[start])
            path[end].append(start)
            heapq.heappush(pq, (d[end], end))

# 방문한 노드번호들 리스트에 마지막 노드번호 추가
path[E].append(E)

# 출력
print(d[E])
print(len(path[E]))
print(' '.join(map(str, path[E])))

