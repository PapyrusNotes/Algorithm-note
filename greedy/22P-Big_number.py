# 출처 : https://programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    ###################################
    # 제거할 작은 숫자들 기준
    small_numbers = [0]*k
    small_numbers[0] = number[0]
    for num in number:
        if small_numbers[0] > num:
            insert(small_numbers, num)

    ###################################
    # 남길 큰 숫자들 기준
    big_numbers = [0]*(len(number)-k)
    big_numbers[0] = number[0]
    for n in number:
        if n > big_numbers[0]:
            insert(big_numbers, n)



    answer = ''
    return answer


def main():
    number1 = "1924"
    k1 = 2

    number2 = "1231234"
    k2 = 3

    number3 = "4177252841"
    k3 = 4

    number4 = "41231"
    k4 = 5

    print(solution(number1, k1))
    return 0


if __name__ == '__main__':

    main()
