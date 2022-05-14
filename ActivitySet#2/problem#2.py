
def add(a, b):
    return (a,b)


def output(a, b, sum):
    pass  # ...


def main():
    a, b = input_two_numbers()
    sum = add(a, b)

    output(a, b, sum)


if __name__ == '__main__':
    main()
