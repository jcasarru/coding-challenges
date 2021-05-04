'''
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
and makes a new list of only the first and last elements of the given list. 

For practice, write this code inside a function.
'''

def get_tail(a):
    return a[-1]

def get_head(a):
    return a[0]

def get_both(a):
    return a[::len(a)-1]

def get_list(help_text="Input a list (numbers separated by whitespace): "):
    return list(input(help_text))


if __name__ == "__main__":
    # list example
    # a = [5, 10, 15, 20, 25]
    a = get_list()
    sublist1 = [get_head(a), get_tail(a)]
    print(f'One way: {sublist1}')
    
    sublist2 = get_both(a)
    print(f'Better way: {sublist2}')