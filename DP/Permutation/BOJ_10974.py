def print_permu(choosed):
    for n in choosed:
        print(n, end=' ')
    print()


def permutation(l):
    if l == N:
        print_permu(choosed)
        return

    for i in range(0, N):
        if using[i]:
            continue
        choosed.append(lst[i])
        using[i] = True
        permutation(l + 1)

        using[i] = False
        choosed.pop()


N = int(input())
lst = [n for n in range(1, N + 1)]

choosed = []

using = [False] * N

permutation(0)
