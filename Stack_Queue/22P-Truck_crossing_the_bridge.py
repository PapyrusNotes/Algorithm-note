# https://programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque


def weight_on_bridge(bridge):
    sum = 0
    for truck in bridge:
        sum += truck
    return sum


def solution(bridge_length, weight, truck_weights):
    answer = 0
    capacity = bridge_length
    bridge = deque()

    while (truck_weights):
        if (truck_weights[0] + weight_on_bridge(bridge) <= weight) and (capacity > 0):
            del truck_weights[0]
            capacity -= 1
            bridge.append(truck_weights[0])
        else:
            bridge.popleft()
            capacity += 1
        answer += 1

    return answer