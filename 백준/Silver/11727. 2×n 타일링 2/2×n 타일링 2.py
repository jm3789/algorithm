#dp
#memo

# 1 --> 1
# 2 --> 3
# 3 --> 5

n = int(input())

if n == 1:
    print(1)

elif n == 2:
    print(3)
    
else:
    memo = [0 for _ in range(n+1)]
    memo[1] = 1
    memo[2] = 3
    if n >= 3:
        for i in range(3, n+1):
            memo[i] = memo[i-2] * 2 + memo[i-1]
    print(memo[n] % 10007)