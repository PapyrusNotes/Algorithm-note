# recursive top-down approach with memoization

N = 10                          # Input
memoization = [-1]*(N+1)


def fibonacci_recur(n):
    if n == 1 or n == 2:
        return 1

    if memoization[n] != -1:
        return memoization[n]

    memoization[n] = fibonacci_recur(n-1) + fibonacci_recur(n-2)

    return memoization[n]


def main():
    print(fibonacci_recur(n=N))
    return 1


if __name__ == '__main__':
    main()
