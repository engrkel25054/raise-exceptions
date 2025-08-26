# Program specification

def find_an_even(L):
    """
    Assumes L is a list of integer numbers.
    Returns the first even number in L.
    Raises ValueError if L does not contain an even number.
    """
    for num in L:
        if num % 2 == 0:
            return num
    raise ValueError(L, "does not contain an even number")

list_1 = [35, 47, 59, 62, 78, 89, 9]
list_2 = [13, 35, 57, 79, 93]


print("list_1:", find_an_even(list_1))
print("list_2:", find_an_even(list_2))