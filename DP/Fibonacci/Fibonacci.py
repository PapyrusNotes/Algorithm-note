# recursive dfs version
def fibonacci_recur(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci_recur(n - 1) + fibonacci_recur(n - 2)


def main():
    print(fibonacci_recur(5))
    return 1


if __name__ == '__main__':
    main()
