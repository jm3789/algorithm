def solution(numbers):
    # answer 배열 크기 미리 정해두기
    answer = [-1 for _ in range(len(numbers))]
    # 스택
    stack = []
    for i in range(len(numbers)-1, -1, -1):
        num = numbers[i]
        while len(stack) > 0:
            if stack[-1] <= num:
                stack.pop()
            else: # stack[-1] > num:
                answer[i] =  stack[-1]
                stack.append(num)
                break
        if len(stack) == 0:
            answer[i] = -1
        stack.append(num)
    return answer