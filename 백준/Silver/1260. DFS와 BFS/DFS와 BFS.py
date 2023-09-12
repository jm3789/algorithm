import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())

link_map = [[False] * N for _ in range(N)]

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    # 정점 A와 B를 연결
    link_map[A-1][B-1] = True
    link_map[B-1][A-1] = True

def dfs(A):
    visited = [False] * N
    dfs_recursion(A, visited)

def dfs_recursion(A, visited):
    visited[A-1] = True
    print(A, end=' ')
    for i in range(N):
        if link_map[A-1][i]:
            B = i+1  # 정점 A와 B가 연결되어 있음 
            if visited[B-1]:
                continue
            dfs_recursion(B, visited)

def bfs(A):
    visited = [False] * N
    bfs_queue = deque()

    visited[A-1] = True  # 첫 정점에서 실행
    print(A, end=' ')
    for i in range(N):
        if link_map[A-1][i]:
            B = i+1
            bfs_queue.append(B)

    while bfs_queue: # 큐에 아무것도 없을 때까지 실행
        A = bfs_queue.popleft()
        if visited[A-1]:
            continue
        visited[A-1] = True
        print(A, end=' ')
        for i in range(N):
            if link_map[A-1][i]:
                B = i+1
                bfs_queue.append(B)

dfs(V)
print('')
bfs(V)