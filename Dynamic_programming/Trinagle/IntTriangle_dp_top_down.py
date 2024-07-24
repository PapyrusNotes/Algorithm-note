# https://school.programmers.co.kr/learn/courses/30/lessons/43105
triangle_input = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]


def recur(triangle, row, i, dp_table):
    if row >= len(triangle):
        return 0
    l_branch = triangle[row][i] + recur(triangle, row + 1, i)
    r_branch = triangle[row][i] + recur(triangle, row + 1, i + 1)
    return max(l_branch, r_branch)


def solution(triangle):
    max_sum = 0
    row = 0
    i = 0
    dp_table_n = 0

    for row in triangle:
        dp_table_n += sum(row)

    dp_table = [-1]*dp_table_n

    return recur(triangle, row, i, dp_table)


# TODO : 2*row + 1 , 2*row + 2


print(solution(triangle_input))
