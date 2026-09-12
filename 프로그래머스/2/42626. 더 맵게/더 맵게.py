import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    while len(scoville) > 1:
        a = heapq.heappop(scoville)
        if a >= K:
            return cnt
        else:
            cnt += 1
            b = heapq.heappop(scoville)
        heapq.heappush(scoville, a + 2*b)
    if len(scoville) == 1:
        return cnt if scoville[0] >= K else -1