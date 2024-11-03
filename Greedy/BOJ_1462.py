N, M = input().split()
N = int(N)
M = int(M)
obl = list(map(int, input().split()))

sl = 0
minw = 0

obl = sorted(obl)
nbl = sorted([-n for n in obl if n < 0 ])
pbl = [n for n in obl if n > 0 ]

#print(nbl)
#print(pbl)

mnbl = 0
mpbl = 0

if nbl:
    mnbl = nbl[-1]
if pbl:
    mpbl = pbl[-1]

#print(mnbl, mpbl)

if mnbl>mpbl:
    for n in range(len(nbl)-1, -1, -M):
        if n == len(nbl)-1:
            minw += nbl[n]
        else:
            minw += nbl[n]*2

    for n in range(len(pbl)-1, -1, -M):
        minw += pbl[n]*2
else:
    for n in range(len(pbl)-1, -1, -M):
        if n == len(pbl)-1:
            minw += pbl[n]
        else:
            minw += pbl[n]*2

    for n in range(len(nbl)-1, -1, -M):
        minw += nbl[n]*2

print(minw)
