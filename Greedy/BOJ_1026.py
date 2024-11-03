N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

mined = [False]*N
A = sorted(A, reverse=True)
S = 0
ti = -1


for i in range(0, N):
    tmin = 10000
    for j in range(0, N):
        if not mined[j]:
            if A[i]*B[j] < tmin:
                tmin = A[i]*B[j]
                ti = j
    S += tmin
    mined[ti] = True

print(S)
