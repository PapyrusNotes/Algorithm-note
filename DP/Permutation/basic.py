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

""""
재귀 함수를 호출하는 과정에서 Combination과 Permutation의 차이

전제 : 대상 리스트는 정렬된 상태.

combination f(index, level)
동일한 수는 포함하지 않고 for문이 앞으로 진행돼야하므로 level+1 이외에 index+1을 전달하여
이전애

permutation f(level)
동일한 수는 포함하지 않지만 순서가 다른 것도 다른 것으로 인정하므로 level+1를 전달하고
for 문의  범위를 combination처럼 index 부터가 아니라 0부터 N까지 range(0,N) 순회하게한다.
단, 이럴 때, 같은 수도 순회하므로 중복해서 수를 뽑기 때문에
check = [False]*N로 이용하여 현재 사용중인 원소를 검사한다.
check[k] = True -> index k 원소가 사용중
check[k] = False -> index k 원소가 사용중이지 않음.
"""
