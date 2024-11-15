# heapq 모듈: 최소 힙의 형태로 정렬
import heapq
import sys

input = sys.stdin.readline

n = int(input())

min_heap = []
for _ in range(n):
    x = int(input())
    if x == 0: 
        print(heapq.heappop(min_heap) if min_heap else 0)
    else: 
        heapq.heappush(min_heap, x)