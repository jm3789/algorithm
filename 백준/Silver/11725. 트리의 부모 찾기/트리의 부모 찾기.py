# 트리 상에서 연결: 부모가 하나
# DFS

from collections import deque

N = int(input())
node_parents = [0] * (N + 1)  # 0번째 인덱스는 사용하지 않음, 1번째 인덱스가 루트 노드
node_parents[0] = -1  # 사용하지 않는 인덱스
node_parents[1] = -1  # 루트 노드의 부모는 -1로 설정
node_map = [ [] for _ in range(N + 1)]  # 0번째 인덱스는 사용하지 않음, 1번째 인덱스가 루트 노드

for _ in range(N-1):
    a, b = map(int, input().split())
    node_map[a].append(b)
    node_map[b].append(a)

stack = deque()
stack.append(1)
while stack:
    node = stack.pop()
    for child in node_map[node]:
        if node_parents[child] == 0:  # 아직 방문하지 않은 노드
            node_parents[child] = node
            stack.append(child)

for parent in node_parents[2:]:
    print(parent)
