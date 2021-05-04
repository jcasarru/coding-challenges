'''
This exercise is Part 1 of 4 of the birthday data exercise series. 
The other exercises are: Part 2, Part 3, and Part 4.

For this exercise, we will keep track of when our friend’s birthdays are, 
and be able to find that information based on their name. 
Create a dictionary (in your file) of names and birthdays. 
When you run your program it should ask the user to enter a name, 
and return the birthday of that person back to them. 
The interaction should look something like this:

>>> Welcome to the birthday dictionary. We know the birthdays of:
Albert Einstein
Benjamin Franklin
Ada Lovelace
>>> Who's birthday do you want to look up?
Benjamin Franklin
>>> Benjamin Franklin's birthday is 01/17/1706.

Happy coding!
'''


if __name__ == "__main__":
    birthdays = {
                    'Ada': '12/10/1815',
                    'Albert': '03/14/1879',
                    'Benjamin': '01/17/1706'
                }
    print('Welcome to the birthday dictionary. We know the birthdays of:')
    # for key, value in birthdays.items():
    #     print(key, ': ', value)

    for key in birthdays:
        print(key)

    who = input("Who's birthday do you want to look up? ")

    if who in birthdays.keys():
        print(f'{who}\'s birthday is {birthdays[who]}')
    else:
        print(f'I don\'t know {who} birthday')