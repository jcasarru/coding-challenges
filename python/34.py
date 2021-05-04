'''
This exercise is Part 2 of 4 of the birthday data exercise series. 
The other exercises are: Part 1, Part 3, and Part 4.

In the previous exercise we created a dictionary of famous scientists’ birthdays. 
In this exercise, 
modify your program from Part 1 to load the birthday dictionary from a JSON file on disk, 
rather than having the dictionary defined in the program.

Bonus: Ask the user for another scientist’s name and birthday to add to the dictionary, 
and update the JSON file you have on disk with the scientist’s name. 
If you run the program multiple times and keep adding new names,
 your JSON file should keep getting bigger and bigger.
'''


import json

def load_json(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    return data

def dump_json(json_file, data):
    with open(json_file, 'w') as f:
        json.dump(data, f)


if __name__ == "__main__":
    birthdays_data = 'resources/birthdays.json'
    birthdays = load_json(birthdays_data)
    print('Welcome to the birthday dictionary. We know the birthdays of:')


    for key in birthdays:
        print(key)

    who = input("Who's birthday do you want to look up? ")

    if who in birthdays.keys():
        print(f'{who}\'s birthday is {birthdays[who]}')
    else:
        print(f'I don\'t know {who}\'s birthday')
        if who not in birthdays.keys():
            answer = input("Enter yes if I should add it to the dictionary? ")

            if answer == 'yes':
                birthday = input("Enter {who}'s birthday (MM/DD/YYYY): ")
                birthdays[who] = birthday
                dump_json(birthdays_data, birthdays)
                print('File updated!')
        # else:
        #     print('Thank you!')
