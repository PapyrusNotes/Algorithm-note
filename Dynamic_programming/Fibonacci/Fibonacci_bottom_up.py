# for-loop bottom-up approach with dp_table

N = 10  # Input


def fibonacci(n):
    dp_table = [-1]*(n+1)
    dp_table[1] = 1
    dp_table[2] = 1

    for i in range(3, n+1):
        dp_table[i] = dp_table[i-1] + dp_table[i-2]

    return dp_table[n]


def main():
    print(fibonacci(n=N))
    return 1


if __name__ == '__main__':
    main()
