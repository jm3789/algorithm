# BFS
from collections import deque

N, M = map(int, input().split())
mat = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    s = input()
    for j in range(M):
        mat[i][j] = int(s[j])
visited = [[[False, False] for _ in range(M)] for _ in range(N)]

queue = deque()
queue.append((0, 0, 1, 0))  # (x, y, cnt, wall)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

ans = -1

while queue:
    x, y, cnt, wall_cnt = queue.popleft()

    if x == N - 1 and y == M - 1:
        # 도착 지점에 도달한 경우
        ans = cnt
        break

    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]

        # 범위를 벗어남: 스킵
        if next_x < 0 or next_x >= N or next_y < 0 or next_y >= M:
            continue

        # 벽이 없는 경우
        if mat[next_x][next_y] == 0:  
            # 이미 방문함: 스킵
            if visited[next_x][next_y][wall_cnt]:  
                continue
            # 방문하지 않은 경우: 방문 처리
            visited[next_x][next_y][wall_cnt] = True
            queue.append((next_x, next_y, cnt + 1, wall_cnt))

        # 벽이 있는 경우: 
        else:  
            # 벽을 부술 수 있는 경우에만 진행
            if wall_cnt == 0:
                # 이미 방문함: 스킵
                if visited[next_x][next_y][wall_cnt + 1] is True:  
                    continue    
                # 방문하지 않은 경우: 방문 처리
                visited[next_x][next_y][wall_cnt + 1] = True
                queue.append((next_x, next_y, cnt + 1, wall_cnt + 1))

print(ans)