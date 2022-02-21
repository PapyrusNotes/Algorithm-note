def solution(people, limit):
    answer = 0
    people.sort()
    left = 0                                # 정렬후 좌, 우 커서를 배치하였다.
    right = len(people) - 1
    while left < right:                     # left -> right, right-> left로 움직이면서 교차되는 순간 모든 사람이 탈출한다.
        if people[left] + people[right] <= limit:   # 가장 작은 몸무게, 가장 무거운 몸무게의 합이 한계값을 넘지 않으면
            left += 1                               # 가장 작은 몸무게 인원을 태운다.
            right -= 1                              # 가장 무거운 몸무게 인원을 태운다.
        else:
            right -= 1                              # 그렇지 않으면 가장 무거운 몸무게 인원만 태운다.
        answer += 1
    if left == right:
        answer += 1

    return answer


def main():
    people = [70, 80, 50]
    limit = 100
    print(solution(people, limit))


if __name__ == '__main__':
    main()
