def deque_for_bfs(data: list):
    from collections import deque


def stack_for_dfs(data: list):
    stack = []




def main():

    """
    개행하면서 입력받기
    total_element = int(input('total_element : '))
    data_stream = [0]*total_element
    for i in range(0, total_element):
        data_stream[i] = int(input())
    """

    # 공백 기준으로 한 줄에 입력받기
    data_stream = list(map(int, input().split()))

    deque_for_bfs(data_stream)
    stack_for_dfs(data_stream)


if __name__ == '__main__':
    main()
