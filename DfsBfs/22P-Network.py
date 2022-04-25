# 출처 : https://programmers.co.kr/learn/courses/30/lessons/43162

def all_visited(graph, top, visited) -> bool:
    for node in graph[top]:
        if visited[node]:
            continue
        return False
    return True


def solution(n, computers):
    visited = []
    stack = []

    visited.append(0)
    stack.append(0)

    for v in range(0, n):
        while stack:
            top = stack[-1]
        if all_visited(graph, top, visited):     # 스택 최상단 노드의 인접노드가 전부 방문됐을 때
            print('popped: ', node_stack.pop())  # 최상단 노드 제거
        if v == connection:
            continue
        if connection in visited:
            continue
        stack.append()


def main():
    n = 5
    computers = [[1, 1, 0, 0, 0], [1, 0, 0, 1, 0], [0, 0, 1, 0, 1], [0, 1, 0, 1, 0], [0, 0, 1, 0, 1]]

    print(solution(n, computers))


if __name__ == '__main__':
    main()
