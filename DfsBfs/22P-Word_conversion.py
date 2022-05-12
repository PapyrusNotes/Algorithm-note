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


def all_visited(top, visited, graph):
    for n in graph[top]:
        if visited[n]:
            continue
        else:
            return False
    return True


def solution(begin, target, words):

    if target not in words:
        return 0

    # generate graph
    graph = draw_graph(words)
    n = len(graph)
    min_level = n
    #print('generated graph : ', graph)

    # set departure node
    departure = [i for i, word in enumerate(words) if is_replaceable(begin, word) is True]
    #print('departure node : ', departure)

    # set variables for DFS
    stack = []
    visited = [False]*n

    for node in departure:
        #print(f'start departure {node}')
        level = 0

        stack.append(node)
        visited[node] = True
        level += 1

        while stack:
            top = stack[-1]
            if all_visited(top, visited, graph):
                stack.pop()
                level -= 1
            else:
                for i in graph[top]:
                    if visited[i]:
                        continue
                    if words[i] == target:
                        level += 1
                        if level < min_level:
                            min_level = level
                        stack.pop()
                        level -= 2
                        continue
                    stack.append(i)
                    level += 1
                    visited[i] = True
                    break

    return min_level

def main():

    begin = "hit"
    target = "cog"
    words = ["hot", "dot", "dog", "lot", "log", "cog"]

    print(solution(begin, target, words))


if __name__ == '__main__':
    main()
