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



# Correct case
stack = [1,2,3,4,5,6]
route = []

for i in range(0,len(stack)):
    stack.pop()
    temp = list(stack)
    route.append(temp)
    print('route : ', route)   # route :  [[1, 2, 3, 4, 5], [1, 2, 3, 4], [1, 2, 3], [1, 2], [1], []]

```
