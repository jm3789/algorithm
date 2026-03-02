# DFS

from collections import deque

N = int(input())  # 1 < N < 9

words = []
for _ in range(N):
    words.append(input())

is_selectable = [True] * N
stack = deque()
min_length = float('inf')

def dfs(i):
    min_length = float('inf')
    stack.append(add_string(stack[-1], words[i]) if stack else words[i])
    is_selectable[i] = False
    if len(stack) == N:
        min_length = len(stack[-1])
    else: 
        for j in range(N):
            if is_selectable[j]:
                min_length = min(min_length, dfs(j))
    stack.pop()
    is_selectable[i] = True
    return min_length
    
def add_string(s1, s2):
    l = min(len(s1), len(s2))
    for i in range(l, 0, -1):
        if s1[-i:] == s2[:i]:
            return s1 + s2[i:]
    return s1 + s2

for i in range(N):
    min_length = min(min_length, dfs(i))
print(min_length)