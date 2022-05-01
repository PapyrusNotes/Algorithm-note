# 출처 : https://programmers.co.kr/learn/courses/30/lessons/43162

def solution(begin, target, words):
    if target not in words:
        return 0

    word = begin
    level = 0

    while word != target:
        pass

    return level


def main():

    begin = "hit"
    target = "cog"
    words = ["hot", "dot", "dog", "lot", "log", "cog"]

    print(solution(begin, target, words))


if __name__ == '__main__':
    main()
