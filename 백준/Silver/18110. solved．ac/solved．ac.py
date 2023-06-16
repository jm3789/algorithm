import sys

n = int(sys.stdin.readline())

if n == 0:  # 아무 의견이 없는 경우
    difficulty = 0

else:  # 의견이 하나 이상 있는 경우
    # 난이도 의견들을 담은 리스트 생성
    comment_list = [int(sys.stdin.readline()) for _ in range(n)]
    # 리스트를 오름차순으로 정렬
    comment_list.sort()

    # trim: 위 아래에서 각각 제외되는 사람의 수
    # <주의> python의 내장함수 round()의 작동방식은 사사오입이 아님. 0.5를 더한 다음 내림하는 방식으로 사사오입 구현
    trim = int(n * 0.15 + 0.5)
    # 평균 계산
    sum = 0
    for i in range(trim, n-trim):
        sum += comment_list[i]
    difficulty = int(sum/(n-trim*2) + 0.5)

print(difficulty)