# https://programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque


def solution(priorities, location):
    q = deque()
    age = 0
    tgt = location

    for priority in priorities:
        q.append(priority)

    while tgt >= 0:
        flag = False
        popped = q.popleft()

        for priority in q:
            if popped < priority:
                q.append(popped)
                flag = True
                tgt -= 1
                break
        if flag:
            continue
        age += 1

    return age