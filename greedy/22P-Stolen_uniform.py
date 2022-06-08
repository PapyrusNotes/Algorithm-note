# 출처 : https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    answer = 0

    while reserve:
        popped = reserve.pop(0)
        if popped in lost:
            lost.remove(popped)
            answer += 1
        if popped - 1 in lost:
            lost.remove(popped - 1)
            answer += 2
            continue
        if popped + 1 in lost:
            lost.remove(popped + 1)
            answer += 2
            continue

    return answer

def main():
    n = 5
    lost = [2, 4]
    reserve = [1, 3, 5]

    print(solution(n, lost, reserve))

    return 0


if __name__ == '__main__':
    main()
