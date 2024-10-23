a = list(map(int, input().split()))  # 본문제에서는 a에 계산을 통해  휴일 + 휴가 조합들 중 하나의 리스트가 담긴다. for 문중 하나.
satisfaction_list = [1, 2, 3, 4, 5, -1, -2, -5, ]  # 본문제에서는 달력 길이만큼 가중치가 기입되어있음. 이 문제에서는 해당 index 위치에 있는 값이 가중치라고 가정.


def sum_up_section(sat, sti, edi):  # sti-edi까지의 값을 합산값에 반영
    temp_sat = 0
    for i in range(sti, edi):
        temp_sat += sat[i]
    print(f"{sti}~{edi}")
    print("section sum : ", temp_sat)
    temp_sat *= (edi - sti)
    print("final sum : ", temp_sat)
    return temp_sat


def sol(a):  # 연속되는 수이면 (연속되는 숫자 만족도 합) x 연속되는 길이 , 연속되지 않으면 단일 만족도 값을 더 해서 총 합을 반환한다.
    if len(a) == 1:
        return a[0]

    sti = 0
    edi = 1
    total_sat = 0

    while edi < len(a):
        if a[edi - 1] == a[edi] - 1:
            # seq
            edi += 1
        else:
            # not seq
            total_sat += sum_up_section(satisfaction_list, sti, edi)
            print("total_sat :", total_sat)
            print()
            sti = edi
            edi = sti + 1

    # sti ~ 문자열 끝까지 결산
    total_sat += sum_up_section(satisfaction_list, sti, edi)
    print()
    print("total_sat : ", total_sat)
    return total_sat


sol(a)



