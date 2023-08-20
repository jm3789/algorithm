import sys

T = int(sys.stdin.readline())

for _ in range(T):

    N = int(sys.stdin.readline())

    if N >= 33:  # 비둘기집 원리: 학생이 33명 이상이면, 유형이 같은 학생이 무조건 3명 이상 나오게 됨
        students = sys.stdin.readline()  # 필요 없음
        print(0)

    else:
        students = tuple(sys.stdin.readline().split())

        # students[a]와 students[b] 사이의 심리적인 거리를 구하는 함수
        def calculate_distance(a, b):  
            d = 0
            for i in range(4):
                if students[a][i] != students[b][i]:
                    d += 1
            return d
        
        min_distance = 100  # 가장 가까운 세 명의 심리적인 거리
        
        # 세 명을 고름
        for i in range(N-2):
            for j in range(i+1, N-1):
                for k in range(j+1, N):
                    # 해당 세 명의 심리적인 거리를 구해, 가장 가까운지 비교
                    distance = calculate_distance(i, j) + calculate_distance(i, k) + calculate_distance(j, k)
                    if distance < min_distance:
                        min_distance = distance

        print(min_distance)