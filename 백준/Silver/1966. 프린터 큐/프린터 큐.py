import sys

count = int(sys.stdin.readline())

for _ in range (0, count):
    N, M = map(int, sys.stdin.readline().split())

    printer_queue = []
    # 모든 문서의 두번째 값을 0으로 설정
    for number in list(map(int, sys.stdin.readline().split())):
        printer_queue.append([number, 0])
    # N개의 문서 중 M번째에 놓여있는 문서의 두번째 값을 1로 설정
    printer_queue[M][1] = 1

    print_count = 0
    # index = 1
    left = N
    
    while print_count < N:  # 문서를 출력한 횟수가 N보다 작을 동안
        index = 1

        # 두번째 문서부터 가장 오른쪽 문서까지 차례대로 첫번째 문서와 비교
        while index < left:  
            # 첫번째 문서보다 큰 경우
            if printer_queue[index][0] > printer_queue[0][0]:  
                printer_queue.append(printer_queue.pop(0))  # 첫번째 문서를 pop, 큐의 맨 뒤에 재배치
                index = 1  # 안덱스를 1로 바꾸고 계속 while문 진행
                continue
            # 첫번째 문서보다 작거나 같은 경우
            index += 1  # 인덱스를 증가시키고 계속 while문 진행

        # index == left. 첫번째 문서가 가장 클 경우에 진입
        printing = printer_queue.pop(0)  # 첫번째 문서 출력
        left -= 1
        print_count += 1  # 문서의 두번째 값이 1인 경우, 출력할 때 print_count 값을 print하고 종료
        if printing[1] == 1: 
            print(print_count)
            break
