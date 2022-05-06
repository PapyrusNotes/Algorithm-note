# 출처 : https://programmers.co.kr/learn/courses/30/lessons/43162

def is_replaceable(word1, word2) -> bool:
    diff_n = 0
    for i, character in enumerate(word1):
        if character == word2[i]:
            continue
        else:
            diff_n += 1
            if diff_n == 2:
                return False
    return True


def draw_graph(words) -> list:
    n = len(words)
    connection = [[] * i for i in range(0, n)]
    for i in range(0, n):
        for j in range(0, n):
            if i == j:
                continue
            if is_replaceable(words[i], words[j]):
                connection[i].append(j)
    return connection


def solution(begin, target, words):

    graph = draw_graph(words)
    # print(graph)
    # return 0

    if target not in words:
        return 0

    word = begin
    stack = []
    visited = []
    level = 0





def main():

    begin = "hit"
    target = "cog"
    words = ["hot", "dot", "dog", "lot", "log", "cog"]

    print(solution(begin, target, words))


if __name__ == '__main__':
    main()
