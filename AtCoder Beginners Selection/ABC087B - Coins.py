A = int(input())
B = int(input())
C = int(input())
X = int(input())

dp = [[0] * (X+1) for _ in range(4)]
dp[0][0] = 1
coins = [500, 100, 50]
counts = [A, B, C]

for i in range(1, 4):
  coin = coins[i-1]
  count = counts[i-1]
  for j in range(X+1):
    dp[i][j] = dp[i-1][j]
    for k in range(1,count+1):
      if j >= coin*k:
        dp[i][j] += dp[i-1][j-coin*k]
  
print(dp[3][X])