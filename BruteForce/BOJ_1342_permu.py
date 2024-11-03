from itertools import permutations


def has_same_adjacent(c):
    for i in range(len(c) - 1):
        if c[i] == c[i + 1]:
            return True
    return False


S = input()
cs = list(set(permutations(S, len(S))))

ans = 0
for c in cs:
    if not has_same_adjacent(c):
        ans += 1

print(ans)

# 메모리 초과
# Test case 4 경우 2.9s 소요 > 시간 제한 2초
# 다른 방법 필요
