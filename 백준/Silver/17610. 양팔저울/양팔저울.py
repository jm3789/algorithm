k = int(input())
weights = list(map(int, input().split()))

able_list = []
for _ in range(sum(weights) + 1):
    able_list.append(False)
able_list[0] = True

# 무게 weights[i]인 추가 추가되었을 때, 가능한 무게들을 True로 처리하는 함수
def check(i, left, right):
    if i == k:
        return
    w = weights[i]
    # 1. 사용하지 않음
    res = right - left
    if res > 0: able_list[res] = True
    check(i+1, left, right)
    # 2. 왼쪽 저울(그릇)에 올리기
    res = right - (left + w)
    if res > 0: able_list[res] = True
    check(i+1, left + w, right)
    # 3. 오른쪽 저울(그릇x)에 올리기
    res = (right + w) - left
    if res > 0: able_list[res] = True
    check(i+1, left, right + w)

check(0, 0, 0)
print(able_list.count(False))