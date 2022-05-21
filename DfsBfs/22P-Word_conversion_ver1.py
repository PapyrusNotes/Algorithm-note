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
    if diff_n == 1:
        return True
    else:
        return False


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


def near_target(index, graph, target_i):
    for node in graph[index]:
        if node == target_i:
            return True
    return False


# target 문자열의 index를 반환하는 함수. 수행 시간 감소 효과.
def get_target_i(target, words):
    for i, word in enumerate(words):
        if word == target:
            return i
    return None


def solution(begin, target, words):
    # get target index
    target_i = get_target_i(target, words)
    if target_i is None:
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
        visited = [False] * n

        if depart_p == target_i:
            return 1
        stack.append(depart_p)
        visited[depart_p] = True
        lvl += 1

        while stack:
            print('stack : ', stack)
            top = stack[-1]

            if all_visited(top, visited, graph):
                print('popped : ', stack.pop())
                lvl -= 1
            else:
                if near_target(top, graph, target_i):
                    print('found target')
                    lvl += 1
                    if lvl < min_lvl:
                        min_lvl = lvl
                    stack.pop()
                    lvl -= 2
                else:
                    for node in graph[top]:
                        if visited[node]:
                            continue
                        else:
                            stack.append(node)
                            visited[node] = True
                            lvl += 1
                            break
    return min_lvl


def main():
    begin = "hot"
    target = "lot"
    words = ["hot", "dot", "dog", "lot", "log", "cog"]

    print(solution(begin, target, words))


if __name__ == '__main__':
    main()
