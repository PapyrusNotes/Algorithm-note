N = int(input())
s = []
for i in range(0, N):
	s.append(tuple(map(int, input().split())))
ns = sorted(s, key=lambda x: (x[1] * x[2] * x[3], x[1]+x[2]+x[3], x[0]))

for c in range(0, 3):
	print(ns[c][0], end=' ')
