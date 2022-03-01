# https://programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque


def weight_on(bridge):
    total = 0
    for truck in bridge:
        total += truck
    return total


def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque()

    while truck_weights:
        bridge.append(truck_weights[0])
        del truck_weights[0]
        answer += 1

        print('trucks waiting : ', truck_weights)
        print('trucks on bridge : ', bridge)

        if bridge_length == len(bridge):
            bridge.popleft()
            answer += 1
            continue

        if truck_weights:
            if truck_weights[0] + weight_on(bridge) > weight:
                answer += bridge_length - len(bridge)
                bridge.popleft()

        print('trucks waiting : ', truck_weights)
        print('trucks on bridge : ', bridge)

    answer += bridge_length

    return answer


def main():
    bridge_length = 20
    weight = 100
    truck_weights = [10]
    print('answer is ', solution(bridge_length, weight, truck_weights))


if __name__ == "__main__":
    main()
