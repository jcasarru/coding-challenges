'''
Take the code from the How To Decode A Website exercise 
(if you didn’t do it or just want to play with some different code, 
use the code from the solution), 
and instead of printing the results to a screen, write the results to a txt file. 

In your code, just make up a name for the file you are saving to.

Extras:

    Ask the user to specify the name of the output file that will be saved.
'''
import requests
from bs4 import BeautifulSoup as BS


def get_site(url):
    r = requests.get(url)
    return r.text

def beauty_site(html):
    soup = BS(html, features="html.parser")
    return soup

def get_class_elements(soup, classes):
    return soup.find_all(class_=classes)

def get_titles(links):
    titles = []

    for i in links:
        if i.text == '':
            pass
        else:
            titles.append(i.text)
    return titles

def get_titles_from_set(soup, classes):
    titles = []

    for i in classes:
        links = get_class_elements(soup, i)

        for j in get_titles(links):
            titles.append(j)
    
    return titles

def save_news_to_file(filename):
    with open(filename+'.txt', 'w') as file:
        for i, title in enumerate(titles):
            print('Saving new #', i+1, ' - ', title[0:10], '...')
            file.write(str(i+1)+' - '+title+'\n\n')

def ask_for_filename(help_text="How should I name the file with all the news? : "):
    return input(help_text)

if __name__ == "__main__":
    url = 'https://www.nytimes.com/'

    html = get_site(url)

    soup = beauty_site(html)

    classes = ['css-kej3w4', 'css-6p6lnl']

    titles = get_titles_from_set(soup, classes)

    filename = ask_for_filename()

    save_news_to_file(filename)

