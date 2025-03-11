#1 1
#2 1
#3 1
#4 2 #3 + #1
#5 2 #4
#6 3 #5 + #3
#7 4 #6 + #2
#8 5 #7 + #1
#9 7 #8 + #4
#10 9 #9 + #5
#11 12 #10 + #6
#12 16 #11 + #7

T = int(input())
memo = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
for i in range(11, 101):
    memo.append(memo[i-1] + memo[i-5])

for _ in range(T):
    print(memo[int(input())])