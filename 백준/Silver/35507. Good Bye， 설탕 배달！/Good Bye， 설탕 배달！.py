import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    A, B, C, P = 0, 0, 0, 0
    flag = True
    N = int(input())

    for _ in range(N):
        a, b, c, p = map(int, input().split())

        if not flag:
            continue

        need_A = max(a - A, 0)
        need_B = max(b - B, 0)
        need_C = max(c - C, 0)
        time_left = p - P - 1

        if time_left < need_A + need_B + need_C:
            flag = False
        else:
            A = max(A, a)
            B = max(B, b)
            C = max(C, c)
            P += (need_A + need_B + need_C + 1)

    print("YES" if flag else "NO")