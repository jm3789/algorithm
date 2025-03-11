T = int(input())
for _ in range(T):
    p = list(('a' + input()).split('R'))
    p[0] = p[0][1:]
    n = int(input())
    x = input()[1:-1]
    if x == '':
        x = []
    else:
        x = list(map(int, x.split(',')))
    # print('---->', p, n, x)

    left_cnt = 0  # 왼쪽에서 제거할 개수
    right_cnt = 0  # 오른쪽에서 제거할 개수
    reversed = False

    for i in range(len(p)):
        if i > 0:
            reversed = not reversed
        if not reversed:
            left_cnt += len(p[i])
        else:
            right_cnt += len(p[i]) 

    if left_cnt + right_cnt > n:
        # 에러 출력
        print('error')

    else: # 슬라이싱
        if left_cnt == 0 and right_cnt == 0:
            pass
        elif left_cnt == 0:
             x = x[:-1*right_cnt]
        elif right_cnt == 0:
            x = x[left_cnt:]
        else:
            x = x[left_cnt:-1*right_cnt]
        if reversed:
            # 뒤집기 적용
            x.reverse()

        # 출력
        res = '['
        for num in x:
            res += str(num) + ','
        if res[-1] == ',':
            res = res[:-1]
        res += ']'
        print(res)
