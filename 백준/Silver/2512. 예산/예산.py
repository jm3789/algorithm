def lower_bound(arr, target):
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return right

N = int(input())
demands = sorted(list(map(int, input().split())))
budget = int(input())

enough_flag = False
index = float('inf')

while index != 0:  # 남은 지방들에게 모두 똑같이 예산을 나눴을 떄 어떤 지방도 채우지 못한다면 while문을 종료한다
    avg = budget // len(demands)
    if avg >= demands[-1]:
        enough_flag = True
        break
    index = lower_bound(demands, avg)
    budget -= sum(demands[:index])
    demands = demands[index:]

if enough_flag:
    print(demands[-1])
else:
    print(budget // len(demands))