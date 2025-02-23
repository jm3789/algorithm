def solution(nums):
    sosu = [True for _ in range(50000)]
    sosu[0] = False
    sosu[1] = False
    for i in range(2, 50000):
        if sosu[i]:
            baesu = 2*i
            while baesu < 50000:
                sosu[baesu] = False
                baesu += i
            
    sosus = []
    for i in range(2, 50000):
        if sosu[i]:
            sosus.append(i)
            
    answer = 0
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                s = nums[i] + nums[j] + nums[k]
                if s in sosus:
                    # print(str(nums[i]) + str(nums[j]) + str(nums[k]))
                    answer += 1
    return answer