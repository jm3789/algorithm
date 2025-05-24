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

d = [float('inf') for _ in range(N+1)]  # 최단거리 리스트
d[0] = 0
d[S] = 0

# 각 노드들의 이전 노드를 저장하자: 이전 노드를 하나씩 기억하면 전체 경로 역추적 가능
prev = [-1 for _ in range(N+1)]

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
            heapq.heappush(pq, (d[end], end))
            prev[end] = start

path = [E]
prev_node = prev[E]
while prev_node != -1:
    path.append(prev_node)
    prev_node = prev[prev_node]
path.reverse()

# 출력
print(d[E])
print(len(path))
print(' '.join(map(str, path)))
