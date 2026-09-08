import math

# 최소공배수 공식: (a * b) // (최대공약수)
def lcm(a, b):
    return (a * b) // math.gcd(a, b)

def solution(signals):
    # 최소공배수 구하기
    sums = []
    for signal in signals:
        sums.append(sum(signal))
    result = 1
    for summ in sums:
        result = lcm(result, summ)
        
    # 최소공배수만큼 반복: 현재 시간에 모두 노란불인가?
    for now_time in range(1, result):
        is_all_yellow = True
        for signal in signals:
            period = sum(signal)
            leftover = now_time % period
            if not (signal[0] < leftover and leftover <= signal[0] + signal[1]):
                is_all_yellow = False
                break
        if is_all_yellow:
            return now_time

    return -1