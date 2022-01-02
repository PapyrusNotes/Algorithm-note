def deque_for_bfs(data: list):
    from collections import deque


def recur_dfs(graph, v, visited):
    # 방문처리
    visited[v] = True
    print(v, end=' ')

    # v와 연결되어있는 노드들을 재귀적으로 호출
    for i in graph[v]:
        if not visited[i]:
            recur_dfs(graph, i, visited)


def stack_for_dfs(data: list):
    stack = []


def main():

    '''
    그래프 연결정보 표현
    0이 아닌 1번째 노드부터 존재한다고 가정.1에 2,3,8, 2에 1,7이, 3에 1,4,5, 4에 3,5, 5에 3,4, 6에 7, 7에 2,6,8, 8에 1,7연결
    방문 여부 정보 초기화
    처음에는 전부 방문하지 않았으므로 FALSE로 초기화
   '''

    graph = [[], [2, 3, 8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]
    visited = [False]*len(graph)

    # 재귀로 dfs 구현
    # recur_dfs(graph, 1, visited)  # graph, 시작 노드, 방문여부 정보를 매개변수로 넣는다.

    # 스택으로 dfs 구현
    # stack_for_dfs(data_stm)

    # deque로 bfs 구현
    # deque_for_bfs(data_stream)


if __name__ == '__main__':
    main()
