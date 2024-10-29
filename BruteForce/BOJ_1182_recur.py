def search (lev):
	global N, S, arr, choose, ans

	# print("current lvl : ", lev)
	# print("current choose : ", choose)
	# print()

	# base case
	if lev == N:
		if choose and sum(choose) == S:
			ans+=1
		return

	# select elements whose index is lev
	choose.append(arr[lev])
	# print("choosing")
	search(lev+1)
	choose.pop()


	# not choosing element whose index is lev (select next instead)
	# print("not choosing")
	search(lev + 1)


N, S = map(int, input().split())
arr = list(map(int, input().split()))
choose = []
ans = 0

search(0) # recursive method

print(ans)
