def solution(people, limit):
    """
    구명보트를 가장 적게 사용하려면
    한계에 가장 가까운 몸무게 조합을 먼저 계산한 뒤(탐욕적)
    제외하고 나머지 몸무게 조합을 계산해야한다.
    """
    import copy
    survivors = copy.deepcopy(people)
    # survivors = sorted(survivors, reverse=True)  # 큰 몸무게를 가진 사람이 가장 앞에 오게
    n = len(survivors)
    answer = 0

    # people 이 빌때까지 (비면 멈추고 answer 반환)
    # 생존자를 훑으면서 조건에 맞는 두 원소를 리스트에서 제거한다.(2명 구출)
    # 다른 것과 더해서 limit을 만족하는 원소가 없을 때는, 가장 앞의 원소를 뺀다.(1명만 구출)

    while survivors:
        popped = False
        if n == 1:
            answer += 1
            break
        for i in range(1, n):
            weight = survivors[0]+survivors[i]
            if weight <= limit:
                survivors.pop(i)    # 0번째 index를 먼저 pop할 시, 다음 i index 위치가 처음과 달라진다.
                survivors.pop(0)    # 따라서 반드시 i index를 pop하고, 고정 위치의 0번째 index를 pop해야한다.
                answer += 1
                popped = True
                n -= 2
                break
        if not popped:
            survivors.pop(0)
            answer += 1
            n -= 1
    return answer


def main():
    people = [70, 80, 50]
    limit = 100
    print(solution(people, limit))


if __name__ == '__main__':
    main()
