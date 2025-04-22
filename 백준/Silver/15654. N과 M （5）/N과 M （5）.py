# 주어진 배열 내에서 가능한 순열을 출력
# 중복 숫자 비허용

N, M = map(int, input().split())
l = list(map(int, input().split()))
l.sort()
res = []
visited = [False] * N

def dfs(depth):
    if depth == M:
        print(*res)
        return
    for i in range(N):
        if visited[i]:
            continue
        res.append(l[i])
        visited[i] = True
        dfs(depth + 1)
        visited[i] = False
        res.pop()

dfs(0)