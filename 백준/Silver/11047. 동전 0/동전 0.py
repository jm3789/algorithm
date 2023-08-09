# A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수

import sys
N, K = map(int, sys.stdin.readline().split())
coin_list = [int(sys.stdin.readline()) for _ in range(N)]  # 주어진 동전 한 개의 가치 리스트

need = K  # 앞으로 채워야 하는 금액. 0이 되면 종료
count = 0  # 동전의 개수

for coin in list(reversed(coin_list)):  # 가장 큰 단위부터 내림차순으로 진행
    if coin <= need:
        count += need // coin  # need를 해당 단위로 나눈 몫을 count에 기록하고
        need = need % coin   # 나머지가 need가 됨

# 출력
print(count)