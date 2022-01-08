def swap(matrix, row, col):
    tmp = matrix[row][col]
    matrix[row][col] = matrix[col][row]
    matrix[col][row] = tmp


def transpose(matrix: list) -> None:  # 행과 열의 원소를 서로 바꾸는 전치행렬
    """
    :param matrix: 항상 2 x 2 이상의 행렬이 들어온다고 가정
    :return:  return 하지 않음
    """
    n = len(matrix)
    for row in range(0, n-1):               #
        for col in range(row + 1, n):       # transpose의 정의에 맞게 y=-x를 기준으로 행,열 원소를 전치한다.
            swap(matrix, row, col)            # matrix[row][col] <-> matrix[col][row]
    return matrix


def main():
    board = [[1, 0, 1, 35, 9], [4, 16, 17, 121, 11], [50, 52, 101, 103, 43], [190, 1635, 1400, 8, 12],
             [66, 12, 5039, 3102, 17]]
    print('before transpose operation: ', board)
    print('after transpose operation : ', transpose(board))


if __name__ == '__main__':
    main()
