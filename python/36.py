'''
This exercise is Part 4 of 4 of the birthday data exercise series. 
The other exercises are: Part 1, Part 2, and Part 3.

In the previous exercise we counted how many birthdays there are in each month in our dictionary of birthdays.

In this exercise, 
use the bokeh Python library to plot a histogram of which months the scientists have birthdays in! 
Because it would take a long time for you to input the months of various scientists, 
you can use my scientist birthday JSON file. Just parse out the months (if you don’t know how, 
I suggest looking at the previous exercise or its solution) and draw your histogram.

If you are using a purely web-based interface for coding, this exercise won’t work for you, 
since it requires installing the bokeh Python package. 
Now might be a good time to install Python on your own computer.
'''


import json
from bokeh.plotting import figure, show, output_file

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

    output_file("plot.html")

    x = list(months_stats.keys())
    y = list(months_stats.values())

    p = figure()
    p.vbar(x=x, top=y, width=0.5)
    show(p)