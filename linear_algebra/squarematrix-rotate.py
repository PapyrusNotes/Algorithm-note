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


def rotate_180(matrix: list) -> list:
    """
    정방행렬을 오른쪽으로 180도 회전했을 때의 행렬을 반환한다.
    :param matrix: 항상 2 x 2 이상의 행렬이 들어온다고 가정
    :return:  작업완료된 matrix
    """
    n = len(matrix)
    new_matrix = [[0]*n for _ in range(0, n)]

    for row in range(0, n):
        for col in range(0, n):
            new_matrix[n-row-1][n-col-1] = matrix[row][col]

    return new_matrix


def rotate_270(matrix: list) -> list:
    """
    정방행렬을 오른쪽으로 270도 회전했을 때의 행렬을 반환한다.
    :param matrix: 항상 2 x 2 이상의 행렬이 들어온다고 가정
    :return:  작업완료된 matrix
    """
    n = len(matrix)
    new_matrix = [[0]*n for _ in range(0, n)]

    for row in range(0, n):
        for col in range(0, n):
            new_matrix[n-col-1][row] = matrix[row][col]

    return new_matrix


def rotate_360(matrix: list) -> list:
    """
    정방행렬을 오른쪽으로 360도 회전했을 때의 행렬을 반환한다.
    :param matrix: 항상 2 x 2 이상의 행렬이 들어온다고 가정
    :return:  작업완료된 matrix
    """
    return matrix


def print_array(matrix):
    n = len(matrix)
    for i in range(0, n):
        print(matrix[i], end='\n')
    return 'complete'


def main():
    board = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    print('before rotate operation: ', print_array(board))
    print('after rotate operation : ', print_array(rotate_270(board)))


if __name__ == '__main__':
    main()
