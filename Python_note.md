# python3를 다루면서 모르고있던 개념 복습 및 오답 노트

---

- list1에서 list2를 append할 때에는 list2의 메모리 주소를 참조하여 append하므로 list2 원소가 바뀌면 list1 원소도 바뀐다.
list 구조체의 경우 다른 변수가 대입 되었을 때 (해당 변수가 할당 되어 있는 메모리 주소)가 대입되기 때문이다. 
```python
# Wrong case
stack = [0,1,2]
route = []
route.append(stack) # route = [[0,1,2]]

stack = [1,0,2,4]
route.append(stack) # route = [[1,0,2,4]]



# Correct case (by creating new list instance)
stack = [1,2,3,4,5,6]
route = []

for i in range(0,len(stack)):
    stack.pop()
    temp = list(stack)
    route.append(temp)
    print('route : ', route)   # route :  [[1, 2, 3, 4, 5], [1, 2, 3, 4], [1, 2, 3], [1, 2], [1], []]
    
# Correct case (by using list slicing)
stack = [1,2,3,4,5,6]
route = []

for i in range(0,len(stack)):
    stack.pop()
    temp = stack[:]
    route.append(temp)
    print('route : ', route)   # route :  [[1, 2, 3, 4, 5], [1, 2, 3, 4], [1, 2, 3], [1, 2], [1], []]
```

---

- lambda 함수를 사용할 떄
선언과 동시에 사용할 수 있다.
간단한 함수를 인자로 넘겨줄 때 사용한다.
- 구성 형태
lambda arguments: expression
- arguemtns: 인자
- expression: 함수의 반환값.
