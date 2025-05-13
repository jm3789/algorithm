len_of_A, len_of_B = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))
print(len((A-B)|(B-A)))