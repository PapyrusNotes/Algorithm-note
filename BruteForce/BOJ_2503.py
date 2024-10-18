# 숫자 야구

from itertools import permutations


def is_matching(candidate, s):
    for lst in s:
        c = str(lst[0])
        strike = lst[1]
        ball = lst[2]

        strike_n = 0
        ball_n = 0
        condition_ok = False

        for i in range(3):
            if int(c[i]) == candidate[i]:
                strike_n += 1
            elif int(c[i]) in candidate:
                ball_n += 1

        if (strike_n == strike) and (ball_n == ball):
            condition_ok = True
        else:
            condition_ok = False
            return condition_ok

    return condition_ok


N = int(input())
s = []
c = []

for i in range(0, N):
    s.append(tuple(map(int, input().split())))

plst = list(permutations(range(1, 10), 3))
for p in plst:
    if is_matching(p, s):
        c.append(p)

print(len(c))
