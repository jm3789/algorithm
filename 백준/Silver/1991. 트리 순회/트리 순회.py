def dfs_prefix(node):
    if node == '.':
        return
    print(node, end='')
    dfs_prefix(node_dict[node][0])
    dfs_prefix(node_dict[node][1])

def dfs_infix(node):
    if node == '.':
        return
    dfs_infix(node_dict[node][0])
    print(node, end='')
    dfs_infix(node_dict[node][1])

def dfs_postfix(node):
    if node == '.':
        return
    dfs_postfix(node_dict[node][0])
    dfs_postfix(node_dict[node][1])
    print(node, end='')

N = int(input())
node_dict = {}
for _ in range(N):
    a, b, c = input().split()
    node_dict[a] = [b, c]

dfs_prefix('A')
print()
dfs_infix('A')
print()
dfs_postfix('A')
print()