# heapq는 특정 값을 직접 삭제하는 기능이 없음  
# 특정 값을 삭제하려면 list.remove() 후 heapify()가 필요 → O(N)으로 비효율적  
# --> valid 딕셔너리를 사용하여 삭제 여부(해당 숫자가 현재 힙에 몇 개 있는지)를 동기화

import sys
import heapq

T = int(input())
for _ in range(T):
    k = int(input())
    min_heap = []
    max_heap = []
    valid = {}
    for _ in range(k):
        q, num = sys.stdin.readline().split()
        num = int(num)
        if q == 'I':  # 삽입
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -1*num)
            valid[num] = valid.get(num, 0) + 1
        elif q == 'D':  # 삭제
            if num == 1:  # 최대값 삭제
                while max_heap:
                    d = -1*heapq.heappop(max_heap)
                    if valid[d] > 0:
                        valid[d] -= 1
                        break
            else:  # 최소값 삭제
                while min_heap:
                    d = heapq.heappop(min_heap)
                    if valid[d] > 0:
                        valid[d] -= 1
                        break

    # valid에 0인 숫자가 힙에 남아있다면 제거
    while max_heap and valid[-1*max_heap[0]] == 0:
        heapq.heappop(max_heap)
    while min_heap and valid[min_heap[0]] == 0:
        heapq.heappop(min_heap)

    if min_heap and max_heap:
        print(-1*max_heap[0], min_heap[0])
    else:
        print('EMPTY')
        