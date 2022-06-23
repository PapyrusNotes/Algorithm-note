# 출처 : https://programmers.co.kr/learn/courses/30/lessons/42860

def solution(name):
    # n_cursor(커서 이동 조작) + n_alphabet(알파벳 이동 조작) = n_joystick(총 조작 횟수)
    # n_alphabet 고정 , n_cursor 최소시, n_joystick 최소

    answer = 0

    flag_a = False  # 'A' 문자 최초 발견 후 진행중 여부
    count_a = 0

    cursor_move = 0
    char_move = 0

    first_a_index = -1
    end_a_index = 0
    cursor_index = 0

    # 한 번도 'A'가 안 나왔을 때는 어떻게 처리? -> 한 번도 'A'가 안 나왔을 때 안 쓰이는 변수 활용
    # first_a_index가 쓰이지 않았다면, 초기화 값으로 판별하기 (first_a_index = -1)
    # if first_a_index == -1 : cursor_move = len(name) - 1
    for i, character in enumerate(name):
        if character != 'A' and not flag_a:  # 'A' 구간이 아닌 구간의 조건
            if 'A' < character <= 'N':
                char_move += ord(character) - ord('A')
            elif 'N' < character <= 'Z':
                char_move += 13 - (ord(character) - ord('N'))
            cursor_index += 1
            continue
        if character == 'A' and not flag_a:  # 'A' 구간의 시작 조건
            first_a_index = i
            end_a_index = i
            flag_a = True
            count_a += 1
            continue
        if character == 'A' and flag_a:  # 'A' 구간의 연속 조건
            count_a += 1
            continue
        if character != 'A' and flag_a:  # 'A' 구간이 끝나는 조건
            end_a_index = i - 1
            flag_a = False
            if first_a_index - 1 < count_a:  # 커서 이득 조건 : 역으로 되돌아가는 길이 < 이득 길이
                cursor_move = 2 * (first_a_index - 1) + len(name) - i
                break
            else:
                continue

    if first_a_index == -1:
        cursor_move = len(name) - 1
    else:
        for i in range(end_a_index, len(name)):
            if name[i] == 'A':
                continue
            if 'A' < name[i] <= 'N':
                char_move += ord(name[i]) - ord('A')
            elif 'N' < name[i] <= 'Z':
                char_move += 13 - (ord(name[i]) - ord('N'))
            continue

    print(char_move + cursor_move)
    # cursor 조작 횟수 이득 조건
    return answer


def main():
    name1 = "JEROEN"
    name2 = "JAN"
    name3 = "SPORTS"
    print(solution(name2))

    return 0


if __name__ == '__main__':
    main()
