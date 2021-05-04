'''
Write a program (function!) that takes a list and returns a new list that contains 
all the elements of the first list minus all the duplicates.

Extras:

    a) Write two different functions to do this - one using a loop and constructing a list, 
    b) and another using sets.
    c) Go back and do Exercise 5 using sets, and write the solution for that in a different function.
'''

def shrink_list(list_a, list_b):
    return [x for x in list_a if x not in list_b]

def shrink_list_sets(list_a, list_b):
    list_a = set(list_a)
    list_b = set(list_b)
    return sorted(list_a.difference(list_b))

if __name__ == "__main__":
    ex_1 = [5, 10, 15, 20, 25]
    ex_2 = [5, 6, 7, 20, 35, 40, 50, 60]

    # a)
    output = shrink_list(ex_1, ex_2)
    print(output)

    # b)
    output = shrink_list_sets(ex_1, ex_2)
    print(output)

    # c)
    output = list(sorted(set(ex_2).intersection(set(ex_2))))
    print(output)