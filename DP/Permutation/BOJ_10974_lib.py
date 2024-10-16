from itertools import permutations

N = int(input())

# permutation(arr, num)
# arr = target array
# The number of element you'd pick

"""
perm = permutations(range(1, N+1))
for p in perm:
	print(p) 
"""

for permutation in permutations(range(1, N + 1)):
    print(' '.join(map(str, permutation)))
