# Maze

N, M = map(int, input().split())

# maze 입력 + 패딩
maze = []
for i in range(0, N):
    row = [0] + list(map(int, input().split()))
    maze.append(row)
maze = [[0] * (M + 1)] + maze

# 초기화 값 입력
dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
dp[1][1] = maze[1][1]

for j in range(2, M + 1):
    dp[1][j] = maze[1][j] + dp[1][j - 1]

for i in range(2, N + 1):
    dp[i][1] = maze[i][1] + dp[i - 1][1]

# dp table 계산
for i in range(2, N + 1):
    for j in range(2, M + 1):
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + maze[i][j]

print(dp[N][M])

