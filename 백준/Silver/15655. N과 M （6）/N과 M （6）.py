# 주어진 배열 내에서 가능한 조합을 출력

N, M = map(int, input().split())
l = list(map(int, input().split()))
l.sort()
res = []

def dfs(start, depth):
    if depth == M:
        print(*res)
        return
    for i in range(start, N):
        res.append(l[i])
        dfs(i+1, depth + 1)
        res.pop()

dfs(0, 0)