# 주어진 배열 내에서 가능한 순열을 출력
# 중복되는 수열은 한 번만 출력해야 한다!

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
        # 바로 앞 숫자와 값이 같고, 그 앞 숫자를 아직 사용하지 않았다면 중복 수열이므로 건너뛴다
        # 단, i가 0이면 l[i-1]이 l[-1]이 되므로 조건은 i > 0일 때만 확인해야 함
        if i > 0: 
            if l[i] == l[i - 1] and not visited[i - 1]:
                continue
        if visited[i]:
            continue
        res.append(l[i])
        visited[i] = True
        dfs(depth + 1)
        visited[i] = False
        res.pop()

dfs(0)