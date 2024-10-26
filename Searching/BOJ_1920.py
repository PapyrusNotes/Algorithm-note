
def bs(lst, num):
	l = 0
	r = len(lst) - 1
	mid = (l+r)//2

	while l < r:
		if num < lst[mid]:
			r = mid - 1
			mid = (l+r)//2
		elif num > lst[mid]:
			l = mid + 1
			mid = (l+r)//2
		elif num == lst[mid]:
			return 1

	if lst[l] == num:
		return 1

	return 0


N = int(input())
A = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))
A = sorted(A)

for i in range(M):
	print(bs(A, nums[i]))
