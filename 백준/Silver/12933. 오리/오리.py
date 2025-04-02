s = input()
word = "quack"

cnt = 0
pre_s = ""
now_s = s
able = True

while now_s:
    if cnt != 0 and now_s == pre_s:
        able = False
        break

    pre_s = now_s

    # if cnt == 10:
    #     break

    cnt += 1

    now_quack_cnt = 0
    now_valid = [1 for _ in range(len(now_s))]
    for i in range(len(now_s)):
        if now_s[i] == word[now_quack_cnt % len(word)]:
            now_valid[i] = 0
            now_quack_cnt += 1

    if now_quack_cnt % len(word) != 0:
        able = False
        break

    now_s = ""
    for i in range(len(now_valid)):
        if now_valid[i] == 1:
            now_s += pre_s[i]
    # print(cnt, "했더니", now_s, "남음")

print(cnt if able else -1)