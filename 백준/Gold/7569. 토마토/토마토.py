# bfs
from collections import deque

M, N, H = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
# print(box)

# 모든 1을 queue에 넣고
# queue에서 하나씩 꺼내면서 인접한 칸을 확인하고
# 인접 숫자 중 0인 숫자가 있으면 중앙 숫자 + 1 로 바꿔넣기
# queue가 빌 때까지 반복
# 모든 칸을 확인하면서 0이 있으면 -1, 아니면 최대값 - 1 출력

def result(box):
    max_num = 0
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if box[i][j][k] == 0:
                    return -1
                else:
                    max_num = box[i][j][k] if box[i][j][k] > max_num else max_num
    return max_num - 1

queue = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 1:
                queue.append((i, j, k))

while queue:
    x, y, z = queue.popleft()
    # 상
    if x > 0:
        if box[x-1][y][z] == 0:
            queue.append((x-1, y, z))
            box[x-1][y][z] = box[x][y][z] + 1
    # 하
    if x < H - 1:
        if box[x+1][y][z] == 0:
            queue.append((x+1, y, z))
            box[x+1][y][z] = box[x][y][z] + 1
    # 좌
    if y > 0:
        if box[x][y-1][z] == 0:
            queue.append((x, y-1, z))
            box[x][y-1][z] = box[x][y][z] + 1
    # 우
    if y < N - 1:
        if box[x][y+1][z] == 0:
            queue.append((x, y+1, z))
            box[x][y+1][z] = box[x][y][z] + 1
    # 앞
    if z > 0:
        if box[x][y][z-1] == 0:
            queue.append((x, y, z-1))
            box[x][y][z-1] = box[x][y][z] + 1
    # 뒤
    if z < M - 1:
        if box[x][y][z+1] == 0:
            queue.append((x, y, z+1))
            box[x][y][z+1] = box[x][y][z] + 1

print(result(box))