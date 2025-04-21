from itertools import permutations
N, M = map(int, input().split())
for nums in permutations(range(1, N+1), M):
    for num in nums:
        print(num, end=' ')
    print()