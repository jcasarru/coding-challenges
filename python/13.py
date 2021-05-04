'''
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 

Take this opportunity to think about how you can use functions.

Make sure to ask the user to enter the number of numbers in the sequence to generate.

(
    Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the
    sequence is the sum of the previous two numbers in the sequence. 
    The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …
)
'''

def get_size(help_text="Choose the size of you fibonacci sequence: "):
    return int(input(help_text))

def get_fibo(size):

    fibo = [1, 1]
    
    if size <= 0:
        return 'Not a valid length'
    elif size == 1 or size == 2:
        return fibo[:size]
    else:
        for _ in range(0,size-2):
            fibo.append(fibo[-2]+fibo[-1])

        return fibo

if __name__ == "__main__":
    a = get_size()
    fibo = get_fibo(a)
    
    print(fibo)