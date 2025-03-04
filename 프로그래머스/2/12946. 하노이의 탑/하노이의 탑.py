# a b c
def hanoi(a, b, c, n):
    if n == 1:
        return [[a, c]]
    else:  # a c b
        res = hanoi(a, c, b, n-1)
        res.extend([[a, c]])
        res.extend(hanoi(b, a, c, n-1))
        return res

def solution(n):
    return hanoi(1, 2, 3, n)