def solution(people, limit):
    answer = 0
    people.sort()
    left = 0
    right = len(people) - 1
    while left < right:
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
        else:
            right -= 1
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
