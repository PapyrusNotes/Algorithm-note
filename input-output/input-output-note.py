
# 개행하면서 입력받기
def input1():
    total_element = int(input('total_element : '))
    data_stream = [0]*total_element
    for i in range(0, total_element):
        data_stream[i] = int(input())
    return data_stream


if __name__ == '__main__':
    # 개행하며 입력받기
    input_data = input1()
    print(input_data, end=' end of the data\n')

    # 공백 기준으로 한 줄에 입력받기
    input_data = list(map(int, input().split()))
    print(input_data, end=' end of the data')
