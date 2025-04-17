N, K = map(int, input().split(' '))
items = [(0,0)]


for i in range(N):
	w, v = map(int, input().split(' '))
	items.append((w, v))

dp_table = [[0 for _ in range(K + 1)] for _ in range(N + 1)]


for i in range(1, N+1):
	w = items[i][0]
	v = items[i][1]
	for j in range(1, K+1):
		dp_table[i][j] = dp_table[i-1][j]
		if j - w >= 0:
			dp_table[i][j] = max(dp_table[i-1][j], dp_table[i-1][j-w] + v)

print(dp_table[N][K])

