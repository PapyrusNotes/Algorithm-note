vows = ['a', 'e', 'i', 'o', 'u']
choose = []


def is_possible():
    global L, C, choose, s

    vow = 0
    for c in choose:
        vow += (c in vows)
    con = L - vow

    return vow >= 1 and con >= 2


def combination(index, level):
    global L, C, choose, s

    # base case
    if level == L:
        if is_possible():
            print(''.join(choose))
        return

    # recursive case
    for i in range(index, C):
        choose.append(s[i])
        combination(i + 1, level + 1)
        choose.pop()


L, C = map(int, input().split())
s = input().split()

s.sort()

combination(0, 0)
