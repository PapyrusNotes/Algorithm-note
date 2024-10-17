def comp(x):
    # 로직
    return x


def minus(x):
    # 로직
    return -x


arr1 = [4, 2, 3, 1, 5]
print(sorted(arr1))
print(sorted(arr1, key=comp))
print(sorted(arr1, key=minus))
print()
# sorted의 key option에는 정렬의 기준이 되는 함수가 들어간다.

arr2 = [(2, 3), (2, 1), (1, 3), (1, -1), (3, 2)]
print(sorted(arr2))
print(sorted(arr2, key=comp))
print(sorted(arr2, key=lambda x: x))  # 기본값
print(sorted(arr2, key=lambda x: (-x[0], -x[1])))  # 기본값
print()
# tuple 형태의 원소인 경우 원소에 접근을 통해 키 기준을 설정한다.
# 파이썬에서 기본 정렬은 기본적으로 오름차순임
# 배열의 원소가 (3,4,5) 여러 개인 경우 앞에 있는 원소를 우선적으로 비교


"""
인덱스 1인 값을 기준으로 내림차순, 만약 인덱스 1인 값이 같다면,
인덱스 0인 값을 기준으로 오름차순 정렬
"""
arr3 = [(3, 10), (4, 20), (1, 30), (2, 20)]
result = sorted(arr3, key=lambda x: (-x[1], x[0]))
print(result)

