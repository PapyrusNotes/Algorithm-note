# 출처 : https://programmers.co.kr/learn/courses/30/lessons/43162

def is_replaceable(word1, word2) -> bool:
    diff_n = 0
    for i, character in enumerate(word1):
        if character == word2[i]:
            continue
        else:
            diff_n+=1
            if diff_n == 2:
                return False
    return True

def solution(begin, target, words):
    if target not in words:
        return 0

    word = begin
    level = 0

    while word != target:


    return level


def main():

    begin = "hit"
    target = "cog"
    words = ["hot", "dot", "dog", "lot", "log", "cog"]

    print(solution(begin, target, words))


if __name__ == '__main__':
    main()
