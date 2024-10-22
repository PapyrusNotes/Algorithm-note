# Greedy 알고리즘을 적용할 수 없는 동전 문제
# Greedy 알고리즘으로 최적해를 도출할 수 없음 -> Brute force 사용

"""
동전 1,3,4원이 있고 최소한의 동전 개수로 N원을 만드는 문제.
N<=1,000,000 이하의 자연수, 시간제한 1초

1로 4를 만들 수 있으나 3을 4로 바꿀 수 없기 때문에
우선순위를 정할 수 없음.
EX ) 6 = 3을 2번 사용하면 만들어지지만, 4로 바꿀 수 없음

1a + 3b + 4c = N을 만족하는 a,b,c의 순서쌍이 답의 후보
a+b+c가 최소인 경우가 답.
0 <= a <= N
0 <= b <= N/3
0 <= c <= N/4
O(N^3)
"""
INF = int(1e7)  # 0이 7개 -> 1000만

N = 6

coin1, coin3, coin4 = None, None, None
min_use = INF

for a in range(N//1 + 1):
    for b in range(N//3 + 1):
        for c in range(N//4 + 1):
            if 1*a + 3*b + 4*c == N:
                if 1*a + 3*b + 4*c < min_use:
                    min_use = a+b+c
                    coin1 = a
                    coin3 = b
                    coin4 = c

print(f"동전1 사용 횟수 {coin1}")
print(f"동전3 사용 횟수 {coin3}")
print(f"동전4 사용 횟수 {coin4}")
print(f"총 사용 개수 {coin1+coin3+coin4}")

# Faster version
def fast_coin(N):
    