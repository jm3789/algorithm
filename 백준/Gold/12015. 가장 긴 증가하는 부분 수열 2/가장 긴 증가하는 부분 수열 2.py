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

for i in range(N):
    if i == 0:
        l.append(A[i])
    else:
        if A[i] > l[-1]:
            l.append(A[i])
        else:
            # lower bound 찾아서 갱신
            index = lower_bound(l, A[i])
            l[index] = A[i]

print(len(l))
