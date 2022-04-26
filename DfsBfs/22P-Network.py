# 출처 : https://programmers.co.kr/learn/courses/30/lessons/43162

def all_visited(graph, top, visited) -> bool:
    for i, node in enumerate(graph[top]):
        if node != 1:
            continue
        if i in visited:
            continue
        else:
            return False
    return True


def solution(n, computers):
    visited = []
    stack = []
    graph = 0

    for v in range(0, n):
        if v in visited:
            print(f'{v} is already graphed')
            continue
        visited.append(v)
        stack.append(v)
        while stack:
            top = stack[-1]
            if all_visited(computers, top, visited):
                print('popped : ', stack.pop())
            else:
                for i, node in enumerate(computers[top]):
                    if node == 1 and i in visited:
                        continue
                    if node == 1 and i not in visited:
                        stack.append(i)
                        visited.append(i)
                        break
            print('stack status : ', stack)
        graph += 1

    print('The number of graph : ', graph)


def main():
    n = 5
    computers = [[1, 1, 0, 0, 0], [1, 0, 0, 1, 0], [0, 0, 1, 0, 1], [0, 1, 0, 1, 0], [0, 0, 1, 0, 1]]

    print(solution(n, computers))


if __name__ == '__main__':
    main()
