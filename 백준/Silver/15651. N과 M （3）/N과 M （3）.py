# 백트래킹: DFS + 가지치기

N, M = map(int, input().split())
res = []

def dfs(depth):
    if depth == M:
        # 완성된 res 출력
        for num in res:
            print(num, end=' ')
        print()
        return
    for i in range(1, N+1):
        res.append(i)
        dfs(depth + 1)
        res.pop()

dfs(0)