# dp
n = int(input())
tri = []
tri.append([])
for i in range(n):
    tri.append(list(map(int, input().split())))

# 맨 아랫층인 n층부터 2층까지 한 층씩 올라가며 반복
for floor_index in range(n, 1, -1):
    # 각 층에 있는 숫자들을 하나씩 확인
    for num_index in range(0, floor_index):

        # 해당 층의 첫 숫자인 경우 패스
        if num_index == 0:
            continue

        # 바로 윗층의 숫자를 갱신: 두 자식 중 더 큰 숫자를 더해준다
        bigger = max(tri[floor_index][num_index], tri[floor_index][num_index-1])
        tri[floor_index-1][num_index-1] += bigger

print(tri[1][0])