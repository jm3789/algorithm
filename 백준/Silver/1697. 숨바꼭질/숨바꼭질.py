# BFS
# dp로는 못푸나?

from collections import deque

def hide_and_seek(N, K):
    counts = [0 for i in range(0, 100001)]

    queue = deque()
    queue.append(N)
    cnt = 0

    if N == K : 
        return 0

    while counts[K] == 0:
        now = queue.popleft()
        next = [now+1, now-1, now*2]
        # print(now)
        # print(next)
        for n in next:
            if n >= 0 and n <= 100000:
                if counts[n] == 0:
                    counts[n] = counts[now] + 1
                    queue.append(n)
    
    return counts[K]
    
N, K = map(int, input().split())
print(hide_and_seek(N, K))