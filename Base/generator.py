from sys import getsizeof

generator_obj = (i for i in range(1000000))  # generator expression

my_list = [i for i in range(1000000)]

# iterator vs generator
# iterator : items return, 모든 item
# generator : item을 return 하지 않고 state(함수의 local variables)를 기억하면서 return

print(getsizeof(generator_obj))
print(getsizeof(my_list))

# generator 객체 하나
# 전체 데이터 메모리에 올라감

# generator function vs generator expression
"""generator function
yield keyword가 나타나는 모든 함수들
yield keyword는 함수가 아닌 generator obj을 만들도록 지시.
yield는 정지시키는 역할을 하고,
함수 밖의 for 문이 next을 통해 실행시키는 것임.

yield가 return하면서 생기는 generator obj도 iterable하기 때문에
next(generator_obj)로 순회시킬 수 있음

"""

"""generator expression
generator_obj = (i for i in range(1000000)) # generator expression
"""

