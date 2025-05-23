def func(lev):
    global S, chars, cnt, choose, ans

    # base case
    if lev == len(S):
        ans += 1
        return

    # recursive case
    for ch in chars:
        if cnt[ch] == 0:
            continue
        if (not choose) or (choose[-1] != ch):
            choose.append(ch)
            cnt[ch] -= 1
            func(lev+1)
            cnt[ch] += 1
            choose.pop()


S = input()
chars = set()
cnt = dict()

for c in S:
    chars.add(c)
    if c not in cnt:
        cnt[c] = 0
    cnt[c] += 1


choose = []
ans = 0

func(0)

print(ans)
