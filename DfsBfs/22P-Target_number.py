import itertools


def solution(numbers, target):
    answer = 0
    flag = ['P', 'M']
    n = len(numbers)
    permuted = [list(x) for x in itertools.product(flag, repeat=n)]

    for seq in permuted:
        total = 0
        for index, sign in enumerate(seq):
            if sign == 'P':
                total += numbers[index]
            else:
                total -= numbers[index]
        if total == target:
            answer += 1
    return answer


def main():

    numbers = [4, 1, 2, 1]
    target = 4
    print('Solution : ', solution(numbers, target))


if __name__ == '__main__':
    main()
