# 분할정복?

N, r, c = map(int, input().split())

# 0 ~ 2**N , 0 ~ 2**N

# r, c를 보고 각각 0, 1, 2, 3 중 어디에 속하는지 확인
# 0 1
# 2 3 
# 으로 표시
def find(r, c, n):
    if r < 2**n and c < 2**n:
        return 0
    elif r < 2**n and c >= 2**n:
        return 1
    elif r >= 2**n and c < 2**n:    
        return 2
    else:    
        return 3
    
order = [0 for _ in range(N)]
answer = 0

# 만약 N = 3이고 r = 3, c = 4라면 order는 [2, 2, 1], 답은 26
for n in range(N-1, -1, -1):
    order[n] = find(r, c, n)
    if order[n] == 1:
        c -= 2**n
    elif order[n] == 2:
        r -= 2**n
    elif order[n] == 3:
        r -= 2**n
        c -= 2**n
    answer += order[n] * 2**n * 2**n

# print('order:', order)
print(answer)