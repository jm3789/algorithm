prefix = []
infix = []
postfix = []

def dfs(node):
    if node == '.':
        return
    prefix.append(node)
    dfs(node_dict[node][0])
    infix.append(node)
    dfs(node_dict[node][1])
    postfix.append(node)

N = int(input())
node_dict = {}
for _ in range(N):
    a, b, c = input().split()
    node_dict[a] = [b, c]

dfs('A')
print(''.join(prefix))
print(''.join(infix))
print(''.join(postfix))