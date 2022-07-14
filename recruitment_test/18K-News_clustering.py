# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/17677

def solution(str1, str2):
    answer = 0
    return answer


def main():

    # sample 1
    str1 = "FRANCE"
    str2 = "french"
    # answer = 16384

    # sample 2
    str1 = "handshake"
    str2 = "shake hands"
    # answer = 65536

    # sample 3
    str1 = "aa1+aa2"
    str2 = "AAAA12"
    # answer = 43690

    # sample 4
    str1 = "E=M*C^2"
    str2 = "e=m*c^2"
    # answer = 65536

    print(solution(str1, str2))
    return 0


if __name__ == '__main__':

    main()