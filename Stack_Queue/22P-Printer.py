# https://programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque


def solution(priorities, location):
    q = deque()
    flag = False
    age = 0

    for priority in priorities:
        q.append(priority)

    if not q:
        return 0

    while True:
        popped = q.popleft()
        print('popped : ', popped)
        location -= 1
        print('location : ', location)

        for priority in q:
            if popped < priority:
                flag = True
                q.append(popped)
                break

        if not flag:
            age += 1
            if location < 0:
                return age
