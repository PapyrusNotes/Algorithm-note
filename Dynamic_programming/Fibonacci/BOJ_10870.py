def fibo_recursive(n):
    # base case
    if n == 1:
        return 1
    if n == 0:
        return 0

    # recursive case
    return fibo_recursive(n - 1) + fibo_recursive(n - 2)


def fibo_iter_memo(n):
    arr = [-1] * (n + 2)
    arr[0] = 0
    arr[1] = 1

    for i in range(2, n + 1):
        arr[i] = arr[i - 1] + arr[i - 2]

    return arr[n]


def fibo_recur_memo(n):
    global memo

    if memo[n] != -1:
        return memo[n]

    memo[n] = fibo_recur_memo(n-1) + fibo_recur_memo(n-2)
    return memo[n]


print("fibo recursive input : ")
num = int(input())
print(fibo_recursive(num))

# 똑같은 값을 반복해서 계산한다면 배열에 저장하여 재사용한다.
print("fibo iteration + memoization input : ")
num = int(input())
print(fibo_iter_memo(num))

print("fibo recursive + memoization input : ")
num = int(input())
memo = [-1] * (num+2)
memo[0] = 0
memo[1] = 1
print(fibo_recur_memo(num))

