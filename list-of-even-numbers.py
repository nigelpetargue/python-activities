def list_of_even_numbers(length):
    list = []

    for i in range(2, length + 1, 2):
        if i % 2 == 0:
            list.append(i)

    print(list)


list_of_even_numbers(98)
