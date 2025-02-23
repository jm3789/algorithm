# bfs: 큐
from collections import deque

def solution(n, edge): 
    # 해시를 이용해 키 존재 여부를 빠르게 확인
    d = {}
    
    for vertex in edge:
        a = vertex[0]
        b = vertex[1]
        if a not in d: 
            d[a] = []
        if b not in d:
            d[b] = []
        d[a].append(b)
        d[b].append(a)
        
    far = [-1 for _ in range(n+1)]
    far[1] = 0
        
    queue = deque()
    queue.append(1)
    
    while len(queue) > 0:
        now = queue.popleft()
        for v in d[now]:
            if far[v] == -1:
                far[v] = far[now] + 1        
                queue.append(v)
                
    max_far = max(far)
    answer = 0
    for f in far:
        if f == max_far:
            answer += 1
    return answer