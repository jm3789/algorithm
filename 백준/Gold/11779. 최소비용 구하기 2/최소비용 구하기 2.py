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

d = [[float('inf'), []] for _ in range(N+1)]  # [최단거리, [방문한 노드번호들]]
d[0][0] = 0
d[S][0] = 0

pq = []
pq.append((S, 0))  # (출발 노드번호, 현재 최단거리)

while pq:
    # 노드 pop
    start, dist = heapq.heappop(pq)  # dist는 이 노드가 pq로 들어가던 시점에서의 최단거리
    # 이미 다른 더 작은 값으로 갱신되었다면 패스
    if d[start][0] < dist:
        continue

    # 해당 노드 확인
    for end, weight in edges[start]:

        # 최단거리 갱신하면서 pq에 넣기
        if d[start][0] + weight < d[end][0]:
            d[end][0] = d[start][0] + weight
            d[end][1] = copy.deepcopy(d[start][1])
            d[end][1].append(start)
            heapq.heappush(pq, (end, d[end][0]))

# 방문한 노드번호들 리스트에 마지막 노드번호 추가
d[E][1].append(E)

# 출력
print(d[E][0])
print(len(d[E][1]))
for num in d[E][1]:
    print(num, end=' ')
print()
