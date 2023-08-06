import sys
n = int(sys.stdin.readline())

stack = []
answer_cal_list = []
answer_number_list = []
correct_number_list = [int(sys.stdin.readline()) for _ in range(n)]

value = 1  # value: 다음으로 stack에 push되어야 할 값
flag = True  # 입력된 수열을 만들 수 없는 경우 False
i = 0

while flag == True:
    if i >= len(correct_number_list):
        break
    correct_number = correct_number_list[i]

    if len(stack) == 0:
        stack.append(value)
        answer_cal_list.append('+')
        value += 1
    else: 
        # stack의 마지막 값과 correct_number를 비교
        # 더 작으면, value 값 push 수행
        if stack[-1] < correct_number:
            stack.append(value)
            answer_cal_list.append('+')
            value += 1  # 다음 value값 준비
        # 같으면 pop 수행.
        elif stack[-1] == correct_number:
            answer_number_list.append(stack.pop())
            answer_cal_list.append('-')
            i += 1  # correct_number_list의 다음 요소가 correct number가 됨
        # 더 크면 수열을 만들 수 없음
        else: 
            flag = False
            break

if flag == True:
    if answer_number_list != correct_number_list:  # 오류. 완성된 수열이 정답과 다름
        print("ERROR")
    else:
        for cal in answer_cal_list:
            print(cal)
else:  # flag == False
    print("NO")
