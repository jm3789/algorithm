from collections import deque

N = int(input())
info = []
for _ in range(N):
    info.append(list(map(int, input().split())))
# print('info:', info)

def is_able_to_find(start, end, info):
    stack = deque()
    stack.append(start)
    visited = [False for _ in range(N)]
    while stack:
        now = stack.pop()
        for i in range(N):
            if info[now][i] == 1 and not visited[i]:
                stack.append(i)
                visited[i] = True
                if i == end:
                    return 1
    return 0

for i in range(N):
    for j in range(N):
        print(is_able_to_find(i, j, info), end=' ')
    print()