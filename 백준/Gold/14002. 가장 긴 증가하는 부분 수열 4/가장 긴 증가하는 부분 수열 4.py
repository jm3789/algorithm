N = int(input())
l = [0 for _ in range(N+1)]  
# l[i]: i번째 원소를 마지막으로 하는 증가하는 부분 수열들 중 가장 긴 것의 길이

A = [0] + list(map(int, input().split()))
for i in range(1, N+1):
    max_num = 0
    for j in range(i):
        if A[j] < A[i]:
            max_num = max(max_num, l[j])
    l[i] = max_num + 1
print(max(l))

# for elem in l:
#     print(elem, end=' ')
# print()

# 부분 수열 출력: 역추적해서 가장 최적화된 부분 수열을 찾아야 함
# l[i]가 가장 큰 값부터 시작해서 찾아야 함
ans = []
now = max(l)
for i in range(len(l)-1, 0, -1):
    if l[i] == now:
        ans.append(A[i])
        now -= 1
ans.reverse()
for elem in ans:
    print(elem, end=' ')
print()