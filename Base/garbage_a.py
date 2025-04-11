class A:
    def __init__(self):
        pass

    def __del__(self):
        print("deleted")


def main():
    a = A()
    print("end")


if __name__ == "__main__":
    main()

# end
# deleted (by gc)
