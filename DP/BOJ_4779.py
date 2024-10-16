# CANTOR SET
def func(k):
    # base case
    if k == 0:
        print('-', end="")
        return

    # recursive case
    func(k - 1)
    print(' ' * (3 ** (k - 1)), end="")
    func(k - 1)


nums = []

while True:
    try:
        nums.append(int(input()))
    except EOFError:
        break

for num in nums:
    func(num)
    print()
