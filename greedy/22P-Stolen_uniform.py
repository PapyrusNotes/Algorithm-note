# 출처 : https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    answer = n - len(set(lost + reserve))
    lost.sort()
    reserve.sort()
    while reserve:
        popped = reserve.pop(0)
        if popped in lost:
            try:
                lost.remove(popped)
                answer += 1
                reserve.remove(popped)
                continue
            except ValueError:
                continue
        if popped - 1 in lost:
            try:
                lost.remove(popped - 1)
                answer += 2
                reserve.remove(popped - 1)
                continue
            except ValueError:
                continue
        if popped + 1 in lost:
            try:
                lost.remove(popped + 1)
                answer += 2
                reserve.remove(popped + 1)
                continue
            except ValueError:
                continue
        answer += 1
    return answer


def main():
    n = 7
    lost = [2, 3, 4]
    reserve = [1, 2, 3, 6]

    print(solution(n, lost, reserve))

    return 0


if __name__ == '__main__':
    main()
