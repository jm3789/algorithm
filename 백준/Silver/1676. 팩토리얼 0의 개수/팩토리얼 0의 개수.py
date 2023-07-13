# 5가 몇 개 들어있는지 구하기

N = int(input())

res = 0

for i in range(1, N+1):
    # i가 5로 나누어떨어지면 res값에 1을 더함
    while i % 5 == 0:
        i /= 5
        res += 1

print(res) 
