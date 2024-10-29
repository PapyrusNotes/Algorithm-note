from itertools import combinations

N, S = map(int, input().split())
arr = list(map(int, input().split()))

count = 0
for n in range(1, N+1):
	cans = list(combinations(arr, n))
	for can in cans:
		if sum(can) == S:
			count +=1

print(count)
