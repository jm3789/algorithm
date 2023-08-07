import sys
N, K = map(int, sys.stdin.readline().split())

coin_list = [int(sys.stdin.readline()) for _ in range(N)]  # 주어진 동전 한 개의 가치 리스트
coin_count_list = [0 for _ in range(N)]  # 필요한 동전의 개수들을 담은 리스트
need = K  # 앞으로 채워야 하는 금액. 0이 되면 종료

i = N-1  # 현재 coin_list[i]는 가장 큰 동전 한 개의 가치
while need != 0:
    if coin_list[i] > need:  # 해당 단위 한 개가 need보다 큼
        # i 값이 0이 아니면, 한칸 앞으로 가서 재진행
        if i != 0:
            i -= 1
            continue
        # i 값이 0이면 더 작은 단위가 존재하지 않으므로 
        else:
            # 현재 count가 1 이상인 가장 작은 단위를 찾고, 해당 count 값에 1을 빼줌
            while coin_count_list[i] == 0:
                i += 1
            coin_count_list[i] -= 1 
            # need값에서 해당 단위 한 개만큼을 더해줌
            need += coin_list[i]
            # 한 칸 앞으로 가서 재진행
            i -= 1
    else: # 해당 단위 한 개가 need보다 작음 (=한 개 이상 들어갈 수 있음)
        coin_count_list[i] = need // coin_list[i]  # need를 해당 단위로 나눈 몫을 count에 기록하고
        need = need % coin_list[i]  # 나머지가 need가 됨

# 검산 후 출력
total = 0
for i in range(0, N):
    total += coin_list[i] * coin_count_list[i]
if total == K:
    print(sum(coin_count_list))
else:
    print("ERROR")