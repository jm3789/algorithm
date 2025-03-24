from itertools import combinations

N = int(input())

S = [0 for _ in range(N+1)]
B = [0 for _ in range(N+1)]
for i in range(1, N+1):
    S[i], B[i] = map(int, input().split())

l = [i for i in range(1, N+1)]
ans = float('inf')
for i in l:
    c = combinations(l, i)
    # print(c)
    for ingredients in c:
        sour = 1
        bitter = 0
        for ingredient in ingredients:
            # print(ingredient, end=' ')
            sour *= S[ingredient]
            bitter += B[ingredient]
        res = abs(sour - bitter)
        # print(res)
        ans = res if res < ans else ans 
print(ans)