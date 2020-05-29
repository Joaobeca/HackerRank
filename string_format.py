def print_formatted(number):
    width = len("{0:b}".format(number))
    for i in range(number):
        print('{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}'.format(i + 1, width=width))

if __name__ == '__main__':
    n = int(input("Type a number: "))
    print_formatted(n)