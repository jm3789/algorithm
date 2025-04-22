# 주어진 배열 내에서 가능한 순열을 출력

N, M = map(int, input().split())
l = list(map(int, input().split()))
l.sort()
res = []

def dfs(depth):
    if depth == M:
        print(*res)
        return
    for i in range(N):
        res.append(l[i])
        dfs(depth + 1)
        res.pop()

dfs(0)