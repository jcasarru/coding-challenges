'''
Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file, 
and print out the results to the screen. I have a .txt file for you, if you want to use it!

Extra:

    Instead of using the .txt file from above (or instead of, if you want the challenge), take this .txt file, 
    and count how many of each “category” of each image there are. 
    
    This text file is actually a list of files corresponding to the SUN database scene recognition database, 
    and lists the file directory hierarchy for the images. Once you take a look at the first line or two of the file, 
    it will be clear which part represents the scene category. 
    
    To do this, you’re going to have to remember a bit about string parsing in Python 3. 
    I talked a little bit about it in this post.
'''

import re


def read_file(fullfilepath):
    with open(fullfilepath, 'r') as o_file:
        content = o_file.read()
    return content.split('\n')

def read_lines_to_list(fullfilepath):
    content = []
    with open(fullfilepath, 'r') as o_file:
        lines = o_file.readlines()
        for line in lines:
            content.append(line.strip())
    return content

def count_elements(ilist):
    output = dict()
    for i in set(ilist):
        output[i] = ilist.count(i)
    return output

if __name__ == "__main__":
    print('\n\n')
    print('-'*80)

    print('File #1')
    counts = count_elements(read_lines_to_list('resources/nameslist.txt'))

    for key, value in counts.items():
        print(f'Word "{key}" appears {value} times')

    print('\n\n')
    print('-'*80)
    
    print('File #2')
    counts = read_lines_to_list('resources/Training_01.txt')
    counts = [re.sub('\/\w*.jpg$','',count) for count in counts]
    counts = count_elements(counts)

    for key, value in counts.items():
        print(f'Category "{key[3:]}" contains {value} files')


