import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    if x1 == x2 and y1 == y2:  # 두 원의 중심이 같을 때
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        if r1 + r2 == dist:  # 내접
            print(1)
        elif r1 + r2 < dist:  # 반지름이 작아서 만나지 않음
            print(0)
        else:
            if abs(r1 - r2) == dist:  # 외접
                print(1)
            elif abs(r1 - r2) < dist:  # 두 원이 만남
                print(2)
            else:  # 한 원이 다른 원 안에 있음
                print(0)