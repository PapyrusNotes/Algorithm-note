class Developer:
    name = "Hong Gil Dong"  # class variable, immutable
    tech_stack = []         # class variable, mutable


developer_1 = Developer()
developer_2 = Developer()

developer_2.name = "Kim Ki In"
developer_2.tech_stack.append("Python")

print("Developer Name")
print(f"Class name : {Developer.name}")
print(f"developer_1 class name : {developer_1.name}")
print(f"developer_2 class name : {developer_2.name}")
print("\n")
# Hong Gil Dong , Hong Gil Dong, Kim Ki In

print("Developer tech_stack")
print(developer_1.tech_stack, developer_2.tech_stack)
# ['Python'], ['Python']
"""
instance namespace에서 instance variable을 먼저 찾고
instance variable을 찾을 수 없으면
class namespace에서 class variable을 찾는다.
"""
