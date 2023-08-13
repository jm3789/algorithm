N = int(input())

word_list = []  # 끝말잇기 기록 리스트

for i in range(N):
    word = input()
    word_list.append(word)
    if word == '?':
        idx = i

first_letter = None
last_letter = None
if idx != 0:  # ?의 순서가 첫번째가 아니면, first_letter 변경
    first_letter = word_list[idx-1][-1] 
if idx != N-1:  # ?의 순서가 마지막이 아니면, last_letter 변경
    last_letter = word_list[idx+1][0]

M = int(input())

for _ in range(M):
    word = input()
    if first_letter is not None: 
        if word[0] != first_letter:  # word의 맨 앞자리가 first_letter와 일치하지 않으면 continue
            continue
    if last_letter is not None:
        if word[-1] != last_letter:  # word의 맨 뒷자리가 last_letter와 일치하지 않으면 continue
            continue
    if word in word_list:  # word가 끝말잇기 리스트에 이미 존재하면 continue
        continue
    print(word)