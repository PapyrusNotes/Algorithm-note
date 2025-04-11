d1 = {"k": [1, 2, 3]}
d2 = d1

print(id(d1), id(d2))
# reference id is same

d2["k"].append(99)
d3 = d1.copy()  # this is shallow copy


print(id(d3))
print(d1, d2, d3)

# id(d3) != id(d1)
# {"k":[1, 2, 3, 99]}, {"k":[1, 2, 3, 99]}, {"k":[1, 2, 3, 99]}


import copy

d4 = copy.deepcopy(d1)  # 내부 데이터를 복사
d3["k"].append(199)

print(id(d4))
print(d1, d2, d3, d4)

# id(d4) != d1
# d1, d2, d3 -> {"k":[1, 2, 3, 99, 199]}
# d4 -> {"k":[1, 2, 3]}