def total(a=5, *numbers, **phonebook):
    print('a', a)
    # iterate through all the items in tuple
    for item in numbers:
        print('single_item', item)

    # iterate through all the items in dictionary
    for first, second in phonebook.items():
        print(first, second)

total(10, 1, 2, 3, Jack=1123, John=2231, Inge=1560)