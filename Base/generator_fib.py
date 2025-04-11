from itertools import islice

# islice : 반복 가능한 객체에서 자르고 싶은 만큼 자른다.
# islice ( 반복 가능한 객체, 시작 index, 끝 index )


def fib():
    prev, curr = 0, 1
    while True:
        yield curr
        prev, curr = curr, prev + curr


f = fib()  # generator 인스턴스 반환

list(islice(f, 0 ,10))

# 1. list는 islice() 인스턴스에서 next를 호출 시작
# 2. islice는 f 인스턴스에서 next 호출.
# 3. fib()함수의 코드 실행
# 3.1 prev, curr = 0, 1실행
# 3.2 while loop에서 yield curr 만남
# 3.3 curr 변수에 저장된 값을 생성하고 유휴상태로 들어간다.
# 3.4 이 생성된 값은 islice에 전달되어 생성되고, list는 값 1을 list에 추가 가능
# 3.5 다음값을 islice에 요청, islice는 f에 다음 값을 요청
# 3.6 f는 이전 상태로부터의 유휴상태가 풀리며 prev, curr = curr, prev + curr를 실행
# 3.7 while loop의 다음 반복에 진입하여 yield curr를 만나고 curr의 다음값을 반환
# 4. islice는 마지막에 도달했음을 가리키는 StopIteration 익셉션을 발생시킨다.
# 5. list는 결괏값을 반환한다.
