from itertools import combinations

def print_set(lst):
    for ele in lst:
        print(ele, end=' ')

def lib_comb(s):
    comb = combinations(s, 6)
    for lst in list(comb):
        print_set(lst)
        print()


while True:
    try:
        a = input().split()
        if a[0] == '0':
            break
        choose = []
        k = int(a[0])
        s = [int(num) for num in a[1:]]
        # comb(0, 0)
        lib_comb(s)
        print()
    except EOFError:
        break
