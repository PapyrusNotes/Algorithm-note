N, M = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))

p1 = 0
p2 = 0
cnt = 0
partial_sum = arr[0]

for index, item in enumerate(arr):
    p1 = index

    while partial_sum < M and p2 < N - 1:
        p2 += 1
        partial_sum += arr[p2]

    if partial_sum == M:
        cnt += 1

    partial_sum -= arr[p1]  # l이 한 칸 이동함에 따라 l의 이전 원소를 빼주어 부분합 개념을 유지한다.

print(cnt)
