# 출처 : 2019 국가 교육기관 코딩 테스트, 큰 수의 법칙
# Solution ver2

def solution(n, m, k, data):
    data.sort()
    max_num = data[n-1]
    next_max_num = data[n-2]

    share, remain = divmod(m, k+1)
    iter_sum = k*max_num + next_max_num
    big_num = (share*iter_sum) + (remain*max_num)

    return big_num


def main():

    n, m, k = map(int, input().split())
    data = list(map(int, input().split()))
    print('Biggest number is : ', solution(n, m, k, data))

    return 0


if __name__ == '__main__':
    main()
