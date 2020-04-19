if __name__ == '__main__':
    n = int(input("Numero: "))
    integer_list = map(int, input().split())
    integer_list = hash(tuple(integer_list))
    print(integer_list)
