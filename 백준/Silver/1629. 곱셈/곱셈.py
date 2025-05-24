# 분할정복
# 나머지 분배 법칙
# (A*B) % C = (A%C) * (B%C) % C

A, B, C = map(int, input().split())

def solution(A, B, C):
    if B == 1:
        return A % C

    # 두 개로 분할
    divided = solution(A, B//2, C)

    if B % 2 == 0:  # B가 짝수
        return divided * divided % C
    else:  # B가 홀수
        return divided * divided * (A % C) % C

print(solution(A, B, C))