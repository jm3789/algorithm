import sys
input = sys.stdin.readline

N = int(input())

heights = []
for _ in range(N):
    h = int(input())
    heights.append(h)

max_height = 0
cnt = 0

for i in range(N-1, -1, -1):
    if max_height < heights[i]:
        cnt += 1
        max_height = heights[i]

print(cnt)