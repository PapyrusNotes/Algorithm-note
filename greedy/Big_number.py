# 출처 : 2019 국가 교육기관 코딩 테스트, 큰 수의 법칙

def solution(n, m, k, data):
    data = data.sort()
    max_num = data[n-1]
    next_max_num = data[n-2]

    big_num = 0


def main():

    n, m, k = map(int, input().split())
    data = list(map(int, input().split()))
    print('before n : ', n)
    print('Biggest number is : ', solution(n, m, k, data))
    print('after n : ', n)
    return 0


if __name__ == '__main__':
    main()
