"""
https://school.programmers.co.kr/learn/courses/18/lessons/1878

세 점의 좌표가 주어졌을 때 나머지 한 점의 좌표를 구한다.
"""


def solution(v):
    answer = []
    x = []
    y = []

    for c in v:
        if c[0] not in x:
            x.append(c[0])
        else:
            x.remove(c[0])
        if c[1] not in y:
            y.append(c[1])
        else:
            y.remove(c[1])
    answer = x + y
    return answer
