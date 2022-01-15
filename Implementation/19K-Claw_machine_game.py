# 출처 : https://programmers.co.kr/learn/courses/30/lessons/64061
def rotate_90(board: list) -> list:
    n = len(board)
    new_matrix = [[0]*n for _ in range(0, n)]

    for row in range(0, n):
        for col in range(0, n):
            new_matrix[col][n-row-1] = board[row][col]

    return new_matrix


def pop_zeros(board):
    n = len(board)
    for row in range(0, n):
        while board[row][-1] == 0:
            board[row].pop()
    print(board)
    return board


def calibrate_moves(moves):
    for i in range(len(moves)):
        moves[i] -= 1
    print('after calibrated moves : ', moves)
    return moves


def solution(board, moves):
    answer = 0
    board = rotate_90(board)
    board = pop_zeros(board)
    moves = calibrate_moves(moves)
    bucket = []

    while moves:
        action = moves.pop()
        if board[action]:
            doll = board[action].pop()
            bucket.append(doll)
            if len(bucket) >= 2 and bucket[-1] == bucket[-2]:
                bucket.pop()
                bucket.pop()
                answer += 2

    return answer


def main():
    board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
    moves = [1, 5, 3, 5, 1, 2, 1, 4]
    print('solution is ', solution(board, moves))
    return 0


if __name__ == '__main__':
    main()
