def print_comb(comb):
    for i in comb:
        print(i, end=" ")
    print()


def comb(index, chosen_n):
    if chosen_n == 6:
        print_comb(choose)
        return

    for i in range(index, k):
        choose.append(s[i])
        comb(i + 1, chosen_n + 1)
        choose.pop()


while True:
    try:
        a = input().split()
        if a[0] == '0':
            break
        choose = []
        k = int(a[0])
        s = [int(num) for num in a[1:]]
        comb(0, 0)
        print()
    except EOFError:
        break
