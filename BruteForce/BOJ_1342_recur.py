def func(lvl):
    global s, ct, fcs, choose, ans

    if lvl == N:
        ans += 1
        return

    if choose:
        for c in fcs:
            if choose[-1] != c and ct[c] > 0:
                choose.append(c)
                ct[c] -= 1
                func(lvl + 1)
                rc = choose.pop()
                ct[rc] += 1
    else:
        for c in fcs:
            choose.append(c)
            ct[c] -= 1
            func(lvl + 1)
            rc = choose.pop()
            ct[rc] += 1


s = input()
N = len(s)
ss = set(s)

ct = {}
choose = []
ans = 0

for ch in ss:
    if 'a' <= ch <= 'z':
        cn = s.count(ch)
        ct[ch] = cn

fcs = sorted(list(ct.keys()))

func(0)

print(ans)
