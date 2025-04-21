N = int(input())
l = [[] for _ in range(N)]
for i in range(N):
    l[i] = list(map(int, input().split()))

l2 = [[0, 0, 0] for _ in range(N)]
for i in range(N):
    if i == 0:
        l2[i] = l[i]
    else:
        l2[i][0] = l[i][0] + min(l2[i-1][1], l2[i-1][2])
        l2[i][1] = l[i][1] + min(l2[i-1][0], l2[i-1][2])
        l2[i][2] = l[i][2] + min(l2[i-1][0], l2[i-1][1])
print(min(l2[N-1][0], l2[N-1][1], l2[N-1][2]))