
N, M = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))

p1 = 0
p2 = 0
cnt = 0

for index, item in enumerate(arr):

	p1 = index
	p2 = index
	tot = arr[p1]

	while (tot < M and p2 < N-1):
		p2 += 1
		tot += arr[p2]

	if tot == M:
		cnt += 1
	elif tot > M:
		continue


print(cnt)
