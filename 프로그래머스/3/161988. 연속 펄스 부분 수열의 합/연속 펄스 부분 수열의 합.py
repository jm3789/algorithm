# DP

def solution(sequence):
    # +-+-+
    memo1 = [0 for _ in range(len(sequence))]
    memo1[0] = sequence[0]
    # -+-+-
    memo2 = [0 for _ in range(len(sequence))]
    memo2[0] = -1*sequence[0]
    
    for i in range(1, len(sequence)):
        if i % 2 == 1:
            memo1[i] = max(memo1[i-1]-sequence[i], -1*sequence[i])
            memo2[i] = max(memo2[i-1]+sequence[i], sequence[i])
        else:
            memo1[i] = max(memo1[i-1]+sequence[i], sequence[i])
            memo2[i] = max(memo2[i-1]-sequence[i], -1*sequence[i])
        
    return max(max(memo1), max(memo2))