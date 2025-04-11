class A:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = set()
        self.workload = ' ' * 128 * 1024 * 1024

    def __del__(self):
        print("delete", self.name)


def main():
    for _ in range(10):
        a = A(name=1)
        a.children.add(A(name=2, parent=a))

    print("end")


if __name__ == "__main__":
    main()

# end
# delete 1
# delete 2


