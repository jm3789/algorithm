# 입력받은 행렬의 0은 -1로 바꿔서 진행
N = int(input())
m = []
for _ in range(N):
    m.append(list(map(int, input().split())))
for i in range(N):
    for j in range(N):
        if m[i][j] == 0:
            m[i][j] = -1

# widths: 1, 2, 4, 8, ..., N/2까지 들어있는 배열
widths = []
w = 1
while w < N:
    widths.append(w)
    w *= 2

# 해당 인덱스로 시작하는 정사각형의 숫자를 커다랗게 처리
# ex
# 1 1 1 1 --> 2 0 0 0
# 2 0 0 0 2 0 0 0 2 0 0 0 2 0 0 0 --> 4 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
def make_this_square_2w(m, i, j, w, axis):
    for k in range(i, i+2*w):
        for l in range(j, j+2*w):
            m[k][l] = 0
    m[i][j] = w*2 *axis

# 행렬에 모든 make_this_square_2w를 적용
# axis가 -1이면 흰색 색종이를 처리, 1이면 파란색 색종이를 처리
def modify_matrix_number(m, axis):
    for w in widths:
        for i in range(0, N, 2*w):
            for j in range(0, N, 2*w):
                # 여기 있는 숫자가 w인지 확인 -> 맞으면 size 늘릴 수 있는지 확인 -> 맞으면 숫자 늘리기
                if m[i][j] == w * axis:
                    if m[i+w][j] == w * axis and m[i][j+w] == w * axis and m[i+w][j+w] == w * axis:
                        make_this_square_2w(m, i, j, w, axis)

modify_matrix_number(m, -1)
modify_matrix_number(m, 1)

'''
for l in m:
    print(l)
'''

# 파란색 색종이의 개수는 양수의 개수, 흰색 색종이의 개수는 음수의 개수
cnt_white = 0
cnt_blue = 0
for i in range(N):
    for j in range(N):
        if m[i][j] < 0:
            cnt_white += 1
        elif m[i][j] > 0:
            cnt_blue += 1

print(cnt_white)
print(cnt_blue)