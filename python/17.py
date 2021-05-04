'''
Use the BeautifulSoup and requests Python packages to print out a list of all 
the article titles on the New York Times homepage.
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


if __name__ == "__main__":
    # url = 'https://www.nytimes.com/es/'
    url = 'https://www.nytimes.com/'

    html = get_site(url)

    # print(url)
    # print(html)

    soup = beauty_site(html)

    classes = ['css-kej3w4', 'css-6p6lnl']

    titles = get_titles_from_set(soup, classes)

    for i, title in enumerate(titles):
        print(i+1, ' - ', title)