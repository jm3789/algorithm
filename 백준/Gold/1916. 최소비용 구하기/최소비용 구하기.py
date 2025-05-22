import heapq
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

edges = [[] for _ in range(N+1)]

for _ in range(M):
    start, end, weight = map(int, input().split())
    edges[start].append((end, weight))  # (도착 노드번호, 비용)

S, E = map(int, input().split())

d = [float('inf') for _ in range(N+1)]
d[0] = 0
d[S] = 0

pq = []
pq.append((S, 0))  # (출발 노드번호, 현재 최단거리)

while pq:
    # 노드 pop
    start, dist = heapq.heappop(pq)  # dist는 이 노드가 pq로 들어가던 시점에서의 최단거리
    # 이미 다른 더 작은 값으로 갱신되었다면 패스
    if d[start] < dist:
        continue

    # 해당 노드 확인
    for end, weight in edges[start]:

        # 최단거리 갱신하면서 pq에 넣기
        if d[start] + weight < d[end]:
            d[end] = d[start] + weight
            heapq.heappush(pq, (end, d[end]))

print(d[E])