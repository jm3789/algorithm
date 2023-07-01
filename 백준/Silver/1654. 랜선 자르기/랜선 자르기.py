# 이분탐색으로 풀기

import sys


# total이 N보다 작지 않게 하는 가장 큰 answer값을 찾아 반환
def binary_search(start, end, answer):
    if start > end:  # 탐색이 끝남. answer값 반환
        return answer
    total = 0
    mid = (start + end)//2
    for cable in cable_list:
        total += cable // mid  # total: 만들 수 있는 mid 길이의 랜선의 총 개수
    if total >= N:  # 랜선의 개수를 만족함: mid값을 answer에 기록하고 mid값 크게.
        answer = mid
        return binary_search(mid+1, end, answer)
    else:  # 랜선의 개수를 만족하지 못함: mid값 작게.
        return binary_search(start, mid-1, answer)


K, N = map(int, sys.stdin.readline().split())

# 가지고 있는 랜선들의 길이를 담은 리스트
cable_list = [int(sys.stdin.readline()) for _ in range(K)]  

start = 1
end = max(cable_list)
answer = 0
print(binary_search(start, end, answer))
