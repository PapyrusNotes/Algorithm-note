# 출처 : https://programmers.co.kr/learn/courses/30/lessons/42860
def  first_A_index(name : str):



def solution(name):
    # n_cursor(커서 이동 조작) + n_alphabet(알파벳 이동 조작) = n_joystick(총 조작 횟수)
    # n_alphabet 고정 , n_cursor 최소시, n_joystick 최소


    answer = 0

    print('full cursor : ', len(name) - 1)
    print('first_A_index : ', first_A_index(name))
    print('end_A_index : ', end_A_index(name))
    print('abbreviated cursor : ', first_A_index(name) * 2 + len(name) - end_A_index(name))
    # switch_or_not = False
    # if first_A_index(name) * 2 + len(name) - end_A_index(name) < len(name) - 1 :

    flag_a = False # 'A' 문자 최초 발견 후 진행중 여부
    count_a = 0
    for i, character in enumerate(name):
        if character != 'A' and not flag_a: # 'A' 구간이 아닌 구간의 조건
            continue
        if character =='A' and not flag_a:  # 'A' 구간의 시작 조건
            first_a_index = i
            flag_a = True
            count_a += 1
            continue
        if character =='A' and flag_a:      # 'A' 구간의 연속 조건
            count_a += 1
            continue
        if character != 'A' and flag_a:     # 'A' 구간이 끝나는 조건
            end_a_index = i
            flag_a = False
            if i < count_a :                # 커서 이득 조건 : 역으로 되돌아가는 길이 < 이득 길이

            continue





    # cursor 조작 횟수 이득 조건
    return answer


def main():
    name1 = "JEROEN"
    name2 = "JAN"

    print(solution(name1))

    return 0


if __name__ == '__main__':
    main()
