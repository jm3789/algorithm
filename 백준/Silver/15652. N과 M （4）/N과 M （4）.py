N, M = map(int, input().split())
res = []

def dfs(start, depth):
    if depth == M:
        for num in res:
            print(num, end=' ')
        print()
        return
    for i in range(start, N + 1):
        res.append(i)
        dfs(i, depth + 1)
        res.pop()

dfs(1, 0)