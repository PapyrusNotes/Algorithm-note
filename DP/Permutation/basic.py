N = 10
R = 3

# 10 P 3
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
check = [False] * N  # 순열의 중복 케이스 방지용 원소 사용 여부
# check[k] = True -> index가 K인 원소가 사용중
# check[k] = False -> index가 K인 원소가 사용중이지 않음
count = 0

choose = []  # 나열한 원소 보관


def permutation(level):
    global count
    if level == R:
        count += 1
        print(choose)
        return

    for i in range(0, N):
        if check[i]:  # 인덱스 i인 원소가 이미 사용중이라면 continue
            continue

        choose.append(lst[i])  # 인덱스가 i인 원소를 선택(추가)
        check[i] = True  # 인덱스가 i인 원소를  사용하고 있으므로 true로 초기화

        permutation(level + 1)  # 다음 for문으로 진입

        check[i] = False
        choose.pop()


permutation(0)
print(count)
