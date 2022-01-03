def deque_for_bfs(data: list):
    from collections import deque


def recur_dfs(graph, v, visited):
    """

    :param graph: 노드와 연결 정보가 입력된 graph
    :param v: 시작 노드 번호
    :param visited: 방문 정보
    :return: None
    재귀함수를 사용하면, 공간 복잡도 면에서
    자기 자신을 계속해서 호출할 때,
    함수가 끝날때까지 호출된 위치를 기억해줘야하는데,
    호출이 반복되면 메모리상 공간이 추가적으로 필요하다.
    주소값을 저장하고 있는 스택이 넘칠 수 있다.
    """
    # 방문처리
    visited[v] = True
    print(v, end=' ')

    # v와 연결되어있는 노드들을 재귀적으로 호출
    for i in graph[v]:
        if not visited[i]:
            recur_dfs(graph, i, visited)


def all_visited(graph, top, visited) -> bool:
    for node in graph[top]:
        if visited[node]:
            continue
        else:
            return False
    return True


def stack_dfs(graph, v, visited):
    node_stack = []
    visited[v] = True
    node_stack.append(v)                    # 시작 노드를 먼저 방문 처리하고 스택에 넣는다.

    while node_stack:                   # 스택이 빌 때까지(스택이 비면 종료한다)
        top = node_stack[-1]            # 스택의 최상단 노드와(node_stack[-1]로 커서 업데이트)

        if all_visited(graph, top, visited):    # 스택 최상단 노드의 인접노드가 전부 방문됐을 때
            print('popped: ', node_stack.pop())                    # 최상단 노드 제거
        else:
            for node in graph[top]:
                if not visited[node]:
                    node_stack.append(node)     # 방문 안 한 노드 하나를 삽입하고 (가장 작은 노드 삽입 기능으로 보완)
                    visited[node] = True        # 방문처리
        print(node_stack)
    print('Iterate ended')


def main():

    """
    그래프 연결정보 표현
    0이 아닌 1번째 노드부터 존재한다고 가정.1에 2,3,8, 2에 1,7이, 3에 1,4,5, 4에 3,5, 5에 3,4, 6에 7, 7에 2,6,8, 8에 1,7연결
    방문 여부 정보 초기화
    처음에는 전부 방문하지 않았으므로 FALSE로 초기화
   """

    graph = [[], [2, 3, 8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]
    visited = [False]*len(graph)

    # 재귀로 dfs 구현
    # recur_dfs(graph, 1, visited)  # graph, 시작 노드, 방문여부 정보를 매개변수로 넣는다.

    # 스택으로 dfs 구현
    stack_dfs(graph, 1, visited)

    # deque로 bfs 구현
    # deque_for_bfs(data_stream)


if __name__ == '__main__':
    main()
