def solution(array, row, col):
    total_max = 1
    for i in range(row):
        row_min = array[i][0]
        for j in range(col):
            if row_min > array[i][j]:
                row_min = array[i][j]
        if total_max < row_min:
            total_max = row_min
    return total_max


def main():
    ROW = int(input())
    COLUMN = int(input())
    array = [[0]*COLUMN for _ in range(ROW)]  # List comprehension으로 2차원 배열 초기화.

    print('Row is', ROW)
    print('Col is', COLUMN)
    print(array)

    '''
    for i in range(ROW):
        for j in range(COLUMN):
            array[i][j] = int(input())  # 개행하면서 입력받을 때
    '''

    for i in range(ROW):
        array[i] = list(map(int, input().split()))  # 공백을 기준으로 한 줄씩 연속 입력 받을 때

    print('Answer is ', solution(array, ROW, COLUMN))


if __name__ == '__main__':
    main()
