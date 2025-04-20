N, K = map(int, input().split(' ')) # 물건 종류의 수, 가방 최대 무게
items = [(0,0)]

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]  # initial dp table

for i in range(N):
	w, v, s = map(int, input().split(' '))  		# weight, value, stock
	if s > 1:
		for _ in range(s-1):
			dp.append([0 for _ in range(K+1)])		# append dp table
			N += 1

	for _ in range(s):
		items.append((w, v)) 						# append item list


for n in range(1, N+1):
	weight = items[n][0]
	value = items[n][1]
	for k in range(1, K+1):
		dp[n][k] = dp[n-1][k]
		if k - weight >= 0:
			dp[n][k] = max(dp[n-1][k], dp[n-1][k-weight] + value)

print(dp[N][K])
