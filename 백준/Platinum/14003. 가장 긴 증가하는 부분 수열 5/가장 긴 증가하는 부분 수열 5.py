def lower_bound(arr, target):
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return right

N = int(input())
A = list(map(int, input().split()))
l = []
# lower bound를 찾을 때마다 index를 저장해놓고, 그 index를 역추적해서 부분 수열을 찾아야 함
bounds = [0 for _ in range(N)]

for i in range(N):
    if i == 0:
        l.append(A[i])
        bounds[i] = 0
    else:
        if A[i] > l[-1]:
            l.append(A[i])
            bounds[i] = len(l) - 1
        else:
            # lower bound 찾아서 갱신
            index = lower_bound(l, A[i])
            l[index] = A[i]
            bounds[i] = index

print(len(l))

# 부분 수열 출력: 역추적해서 가장 최적화된 부분 수열을 찾아야 함
ans = []
now = max(bounds)
for i in range(len(bounds)-1, -1, -1):
    if bounds[i] == now:
        ans.append(A[i])
        now -= 1
ans.reverse()
for elem in ans:
    print(elem, end=' ')
print()