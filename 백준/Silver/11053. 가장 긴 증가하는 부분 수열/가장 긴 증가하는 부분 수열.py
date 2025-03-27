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
