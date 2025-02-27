from collections import deque

n, m = map(int, input().split())

mat = [[] for _ in range(n)]
for i in range(n):
    mat[i] = list(map(int, input().split()))

res = [[-1 for _ in range(m)] for _ in range(n)]


x = 0
y = 0
# x, y에 시작점의 좌표를 저장
for i in range(n):
    for j in range(m):
        if mat[i][j] == 0:
            res[i][j] = 0
        elif mat[i][j] == 2:
            x = i
            y = j
            res[i][j] = 0

queue = deque()
queue.append((x, y))

while queue:
    i, j = queue.popleft()
    if i > 0:
        if res[i-1][j] == -1:
            res[i-1][j] = res[i][j] + 1
            queue.append((i-1, j))
    if i < n-1:
        if res[i+1][j] == -1:
            res[i+1][j] = res[i][j] + 1
            queue.append((i+1, j))
    if j > 0:
        if res[i][j-1] == -1:
            res[i][j-1] = res[i][j] + 1
            queue.append((i, j-1))
    if j < m-1:
        if res[i][j+1] == -1:
            res[i][j+1] = res[i][j] + 1
            queue.append((i, j+1))

for i in range(n):
    for j in range(m):
        print(res[i][j], end=' ')
    print()