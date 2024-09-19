
SUBLIST = "sublist"
SUPERLIST = "superlist"
EQUAL = "equal"
UNEQUAL = "unequal"


def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    elif is_sublist(list_one, list_two):
        return SUBLIST
    elif is_sublist(list_two, list_one):
        return SUPERLIST
    else:
        return UNEQUAL


def is_sublist(smaller, larger):
    if not smaller:
        return True
    for i in range(len(larger) - len(smaller) + 1):
        if larger[i:i + len(smaller)] == smaller:
            return True
    return False

if __name__ == "__main__":
    A = [1, 2, 3]
    B = [1, 2, 3, 4, 5]
    print(sublist(A, B)) 

    A = [1, 2, 3]
    B = [1, 2, 3]
    print(sublist(A, B))  

    A = [1, 2, 3, 4, 5]
    B = [2, 3, 4]
    print(sublist(A, B))

    A = [1, 2, 4]
    B = [1, 2, 3, 4, 5]
    print(sublist(A, B))