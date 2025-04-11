class A:
    def __init__(self):
        pass

    def __del__(self):
        print("delete")


def main():
    a = A()
    del a
    print("end")


if __name__ == "__main__":
    main()

# delete
# end
