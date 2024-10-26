def bs(lst, num):
    """
    lst 내에서 num을 이분탐색을 사용해 찾고 존재 여부를 반환한다.
    :param lst: int 숫자 배열
    num: 찾고자하는 타깃 int 숫자
    :return: Bool
    :rtype: Bool
    """
    l = 0
    r = len(lst) - 1
    mid = (l + r) // 2

    while l < r:
        if num < lst[mid]:
            r = mid - 1
            mid = (l + r) // 2
        elif num > lst[mid]:
            l = mid + 1
            mid = (l + r) // 2
        elif num == lst[mid]:
            return 1

    if lst[l] == num:
        return 1

    return 0
