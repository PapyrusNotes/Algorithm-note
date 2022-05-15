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
    print('generated graph : ', graph)

    # set departure node
    departure = [i for i, word in enumerate(words) if is_replaceable(begin, word) is True]
    print('departure node : ', departure)

    # DFS departure node
    for depart_p in departure:
        min_lvl = n
        lvl = 0
        stack = []
        visited = [False]*n

        stack.append(depart_p)
        visited[depart_p] = True
        lvl += 1

        while stack:
            print('stack : ', stack)
            top = stack[-1]
            flag = False    # top 인덱스를 가지는 노드의 인접노드들의 값들이 target인지 여부
            if all_visited(top, visited, graph):
                print('popped : ', stack.pop())
            else:
                for node in graph[top]:
                    if words[node] == target:
                        print('found target')
                        visited[node] = True
                        flag = True
                        lvl += 1
                        if lvl < min_lvl:
                            min_lvl = lvl
                        lvl -= 1
                        break
                if
                    elif visited[node]:
                        continue
                    else:
                        stack.append(node)
                        visited[node] = True
                        lvl += 1
                        break
    return min_lvl


def main():
    begin = "hit"
    target = "cog"
    words = ["hot", "dot", "dog", "lot", "log", "cog"]

    print(solution(begin, target, words))


if __name__ == '__main__':
    main()
