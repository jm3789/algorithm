import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())

d = [float('inf') for _ in range(V+1)]  # 인덱스가 노드 번호
d[K] = 0  # 시작 노드의 거리 초기화

# 각 노드와 연결되는 간선 정보 저장
edges = {}
for i in range(1, V+1):
    edges[i] = []  
for _ in range(E):
    u, v, w = map(int, input().split())
    edges[u].append((v, w))

pq = []  # 우선순위 큐: [거리, 노드번호] 형태로 저장. 가장 작은 거리의 노드 번호를 반환하도록
heapq.heappush(pq, [0, K])

while pq:
    dist, start = heapq.heappop(pq)  # 출발점으로부터 가장 작은 거리, 노드번호를 pop
    if d[start] < dist:  # 이미 방문한 노드인 경우 스킵
        continue

    for edge in edges[start]:  # start 노드와 연결된 간선에 대한 정보
        end = edge[0]
        weight = edge[1]
        # start 노드에서 end 노드로 가는 거리 갱신
        if d[start] + weight < d[end]:
            d[end] = d[start] + weight
            # 갱신된 거리와 노드번호를 우선순위 큐에 넣음
            heapq.heappush(pq, [d[end], end])

# 결과 출력
for i in range(1, len(d)):
    if d[i] == float('inf'):
        print("INF")
    else:
        print(d[i])