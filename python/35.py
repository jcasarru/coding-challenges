'''
This exercise is Part 3 of 4 of the birthday data exercise series. 
The other exercises are: Part 1, Part 2, and Part 4.

In the previous exercise we saved information about famous scientists’ names and birthdays to disk. 
In this exercise, load that JSON file from disk, extract the months of all the birthdays, 
and count how many scientists have a birthday in each month.

Your program should output something like:

{
	"May": 3,
	"November": 2,
	"December": 1
}
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

    months_to_string = {
                1: "January",
                2: "February",
                3: "March", 
                4: "April",
                5: "May",
                6: "June",
                7: "July",
                8: "August",
                9: "September",
                10: "October",
                11: "November",
                12: "December"
            }

    months_stats = {
            "January": 0,
            "February": 0,
            "March": 0, 
            "April": 0,
            "May": 0,
            "June": 0,
            "July": 0,
            "August": 0,
            "September": 0,
            "October": 0,
            "November": 0,
            "December": 0
        }


    months_statistics = 'resources/months_stats.json'
    birthdays = load_json(birthdays_data)

    months = []

    for key, value in birthdays.items():
        months.append(months_to_string[int(value[:2])])
    
    for month in months:
        months_stats[month] += 1

    for key in list(months_stats):
        if months_stats[key] == 0:
            del months_stats[key]

    print(months_stats)