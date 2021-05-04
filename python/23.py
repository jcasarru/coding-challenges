'''
Given two .txt files that have lists of numbers in them, find the numbers that are overlapping. 
One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of happy numbers up to 1000.

(If you forgot, prime numbers are numbers that can’t be divided by any other number. 
And yes, happy numbers are a real thing in mathematics - you can look it up on Wikipedia. 
The explanation is easier with an example, which I will describe below.)
'''


def read_lines_to_list(fullfilepath):
    content = []
    with open(fullfilepath, 'r') as o_file:
        lines = o_file.readlines()
        for line in lines:
            content.append(line.strip())
    return content

def get_overlaps(list1, list2):
    output = []
    for x in range(0, len(list1)):
        if list1[x] == list2[x]:
            output.append(list1[x])
    return output


if __name__ == "__main__":
    primes = read_lines_to_list('resources/primenumbers.txt')
    happy = read_lines_to_list('resources/happynumbers.txt')

    # if len(primes) > len(happy):
    #     overlap = get_overlaps(happy, primes)
    # else:
    #     overlap = get_overlaps(primes, happy)

    # print(overlap)

    # alt 1
    equals = [x for x in primes for y in happy if x == y]

    # alt 2
    equals = [x for x in primes if x in happy]

    # alt 3
    equals = list(sorted(set(happy).intersection(set(primes))))

    print(equals)