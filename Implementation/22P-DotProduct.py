# 출처 : https://programmers.co.kr/learn/courses/30/lessons/70128

def solution(a, b):
    return sum(map(lambda x: x[0]*x[1], list(zip(a, b))))
