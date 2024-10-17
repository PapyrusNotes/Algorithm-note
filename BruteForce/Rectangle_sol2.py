def solution(v):
    x = v[0][0] ^ v[1][0] ^ v[2][0]
    y = v[0][1] ^ v[1][1] ^ v[2][1]

    return [x, y]


v = [[1, 4], [3, 4], [3, 10]]
print("Solution : ", solution(v))

# XOR Bit calculation
a = 1
b = 2
print(a ^ b)  # 2진수 비트 연산임에 주의할 것
print(1 ^ 2)
print(4 ^ 3)
print(3 ^ 3)
print(4 ^ 3 ^ 3)  # 3 ^ 3 = 0, 4 ^ 3 ^ 3 = 4
