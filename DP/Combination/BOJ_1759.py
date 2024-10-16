def print_pw(pw):
    for c in pw:
        print(c, end='')


def check_comb():
    global vowel_L, consonants_L
    if vowel_L >= 1 and consonants_L >= 2:
        return True
    return False


def insert_check(c):
    global vowel_L, consonants_L, vowels
    if c in vowels:
        vowel_L += 1
    else:
        consonants_L += 1


def pop_check(c):
    global vowel_L, consonants_L, vowels
    if c in vowels:
        vowel_L -= 1
    else:
        consonants_L -= 1


def check_char(c):
    global vowel_L, consonants_L
    if c in vowels:
        vowel_L += 1
    else:
        consonants_L += 1


def pw_comb(index, l):
    # base case
    if l == L:
        if check_comb():
            print_pw(pw)
            print()
        return

    # recursive case
    for i in range(index, C):
        pw.append(s[i])
        insert_check(s[i])
        pw_comb(i + 1, l + 1)
        popped = pw.pop()
        pop_check(popped)


# BOJ 1750
vowels = ['a', 'e', 'i', 'o', 'u']
vowel_L = 0
consonants_L = 0

L, C = (map(int, input().split()))
s = input().split()
s = sorted(s)

pw = []
pw_comb(0, 0)
