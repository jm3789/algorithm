from collections import deque

T = int(input())
for _ in range(T):
    N = int(input())
    if N == 0:
        print(1, 0)
    elif N == 1:
        print(0, 1)
    else:
        deq = deque()
        deq.append((1, 0)) 
        deq.append((0, 1))
        i = 2
        while i <= N:
            deq.append((deq[-1][0] + deq[-2][0], deq[-1][1] + deq[-2][1]))  # 점화식
            i += 1
        cnt_pair = deq.pop()
        print(cnt_pair[0], cnt_pair[1])
        