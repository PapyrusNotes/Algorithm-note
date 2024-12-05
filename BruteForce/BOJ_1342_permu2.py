from itertools import permutations
# 인접 문자들을 확인한 뒤, 나중에 산술적으로 개수를 계산


def fact(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return n*fact(n-1)


S = input()
ans = 0

for candidate in permutations(S):
    ok = True
    for i in range(0, len(S)-1):
        if candidate[i] == candidate[i+1]:
            ok = False
            break
        ans += ok

for i in range(ord('a'), ord('z') + 1):
    ans //= fact(S.count(chr(i)))

print(ans)
