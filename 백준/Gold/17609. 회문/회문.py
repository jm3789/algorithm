def pal(word, left, right, isFirst):
    while left < right:
        if word[left] != word[right]:
            if isFirst:
                if pal(word, left + 1, right, False) == 0 or pal(word, left, right - 1, False) == 0:
                    return 1
            return 2
        left += 1
        right -= 1
    return 0

T = int(input())
for _ in range(T):
    word = input().strip()
    isFirst = True
    print(pal(word, 0, len(word) - 1, isFirst))
