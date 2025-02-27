N = int(input())
l = list(map(int, input().split()))
li = sorted(set(l))  # set을 이용해 중복을 제거하고 정렬

# print(l)
# print(li)

dict_num_cord = {}  # 숫자별 좌표를 저장할 딕셔너리

for i in range(len(li)):
    dict_num_cord[li[i]] = i  # 숫자별 좌표 저장

for num in l:
    print(dict_num_cord[num], end=' ')
print()