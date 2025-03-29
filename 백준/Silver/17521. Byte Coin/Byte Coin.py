n, W = map(int, input().split())

prices = [999] + [0 for _ in range(n)] + [0]
for i in range(1, n+1):
    prices[i] = int(input())

coins = 0

for i in range(1, n+1):
    if prices[i] == prices[i-1]:
        continue
    now = i
    price = prices[now]
    while prices[now] == price:
        now -= 1
    before = prices[now]
    now = i
    while prices[now] == price:
        now += 1
    after = prices[now]
    # 극솟값: 풀매수
    if price < before and price < after:
        coins += W // price
        W %= price
    # 극댓값: 풀매도
    if price > before and price > after:
        W += coins * price
        coins = 0

print(W)
