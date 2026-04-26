N = int(input())

for i in range(N*2):
    part1 = [" "] * N*2
    part1[2*N - i - 1] = "*"

    left = i % N
    part2 = [" "] * N
    part3 = [" "] * N

    if i < N:
        part2[N-1 - left] = "*"
        part3[left] = "*"
    else:
        part2[left] = "*"
        part3[N-1 - left] = "*"

    print("".join(part1) + " " + "".join(part2) + " " + "".join(part3))