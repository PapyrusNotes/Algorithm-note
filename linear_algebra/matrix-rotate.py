def rotate_90(matrix: list) -> list:
    """
    정방행렬을 오른쪽으로 90도 기울였을 때의 행렬을 반환한다.
    :param matrix: 항상 2 x 2 이상의 행렬이 들어온다고 가정
    :return:  작업완료된 matrix
    """
    n = len(matrix)
    new_matrix = [[0]*n for _ in range(0, n)]

    for row in range(0, n):
        for col in range(0, n):
            new_matrix[col][n-row-1] = matrix[row][col]

    return new_matrix


def main():
    board = [[1, 0, 1, 35, 9], [4, 16, 17, 121, 11], [50, 52, 101, 103, 43], [190, 1635, 1400, 8, 12],
             [66, 12, 5039, 3102, 17]]
    print('before rotate operation: ', board)
    print('after rotate operation : ', rotate_90(board))


if __name__ == '__main__':
    main()
