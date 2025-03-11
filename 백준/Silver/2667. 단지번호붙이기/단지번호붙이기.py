from collections import deque

N = int(input())
m = []
for _ in range(N):
    m.append(list(map(int, input())))
# print('m:', m)

q = deque()
answer = []

for i in range(N):
    for j in range(N):
        if m[i][j] != 0:
            q.clear()
            q.append((i, j))
            m[i][j] = 0
            cnt = 0
            while q:
                cnt += 1
                x, y = q.popleft()
                # print('x, y:', x, y)
                # 상하좌우 탐색
                if x > 0:
                    if m[x-1][y] == 1:
                        q.append((x-1, y))
                        m[x-1][y] = 0 
                if x < N-1:
                    if m[x+1][y] == 1:
                        q.append((x+1, y))
                        m[x+1][y] = 0
                if y > 0:
                    if m[x][y-1] == 1:
                        q.append((x, y-1))
                        m[x][y-1] = 0 
                if y < N-1:
                    if m[x][y+1] == 1: 
                        q.append((x, y+1))
                        m[x][y+1] = 0
            answer.append(cnt)

answer.sort()
print(len(answer))
for a in answer:
    print(a)