# https://programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque

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
        location -= 1
        flag = False

        for priority in q:
            if popped < priority:
                flag = True
                q.append(popped)
                if location == -1:
                    location = len(q)
                break

        if not flag:
            if location < 0:
                return age + 1
            age += 1

