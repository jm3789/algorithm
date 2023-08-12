socks_list = []  # 양말 리스트
for _ in range(5): 
    num = int(input())
    if num in socks_list:
        socks_list.remove(num)  # 해당 숫자 양말이 이미 있으면 제거
    else:
        socks_list.append(num)  # 없으면 해당 숫자 추가
print(socks_list[0])
