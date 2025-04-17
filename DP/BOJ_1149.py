N = int(input())
costs = []
for i in range(N):
    cost = list(map(int, input().split()))
    costs.append(cost)
costs = [[0] * 3] + costs
# print(costs)

dp = [[0 for _ in range(3)] for _ in range(N + 1)]
for i in range(3):
    dp[1][i] = costs[1][i]
# print(dp)


for i in range(2, N + 1):
    for j in range(0, 3):
        if j == 0:
            dp[i][j] = min(dp[i - 1][1], dp[i - 1][2]) + costs[i][j]
        elif j == 1:
            dp[i][j] = min(dp[i - 1][0], dp[i - 1][2]) + costs[i][j]
        elif j == 2:
            dp[i][j] = min(dp[i - 1][0], dp[i - 1][1]) + costs[i][j]

print(min(dp[i][0], dp[i][1], dp[i][2]))
