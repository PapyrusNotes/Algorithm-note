# 출처 : https://programmers.co.kr/learn/courses/30/lessons/43162

def travel_network(n, v, computers):
    visited = [False] * n
    stack = []

    return visited


def delete_visited(visited_node, computers):
    for vn in visited_node:
        del computers[vn]
    return computers


def solution(n, computers):
    n_networks = 0

    if n is 0:
        return 0

    # Start traveling networks from computer 0
    while computers:
        visited_node = travel_network(n, 0, computers)
        computers = delete_visited(visited_node, computers)
        n_networks += 1

    return n_networks


def main():
    n = 3
    computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

    print(solution(n, computers))


if __name__ == '__main__':
    main()
