from collections import deque

def solution(numbers, target):
    queue = deque()
    
    queue.append(numbers[0])
    queue.append(-numbers[0])
    
    for i in range(1, len(numbers)):
        for _ in range(len(queue)):
            a = queue.popleft()
            queue.append(a-numbers[i])
            queue.append(a+numbers[i])

    answer = queue.count(target)
    return answer