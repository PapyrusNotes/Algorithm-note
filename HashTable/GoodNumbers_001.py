
N = int(input())
arr = list(map(int, input().split()))
target_numbers = set(arr)


def count_good_num() -> int:
    global arr, target_numbers, N
    count = 0
    checked = set()
    for i in range(0, N-1):
        for j in range(i+1, N-1):
            total = arr[i] + arr[j]
            if total not in checked and total in target_numbers:
                # print(f"arr[i] : {arr[i]} + arr[j] : {arr[j]} = {arr[i]+arr[j]}",)
                checked.add(total)
                count += 1
    return count


answer = count_good_num()
print(answer)

