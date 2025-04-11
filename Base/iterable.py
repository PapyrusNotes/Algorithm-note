x = [1, 3, 4]  # list object which is iterable

y = iter(x)     # iterator instance
z = iter(x)     # iterator instance

print(next(y))
print(next(z))

# iterator : 값 생성기
# next 호출 시, 다음 값 생성

# iter() : iterable을 iterator로 바꾸는 built-in function
# next() : iterator의 다음 item을 반환하는 built-in function

