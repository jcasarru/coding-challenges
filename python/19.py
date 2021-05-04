'''
Using the requests and BeautifulSoup Python libraries, print to the screen the 
full text of the article on this website:
 http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.

The article is long, so it is split up between 4 pages. 
Your task is to print out the text to the screen so that you can read the full 
article without having to click any buttons.

(Hint: The post here describes in detail how to use the BeautifulSoup and 
requests libraries through the solution of the exercise posted here.)

This will just print the full text of the article to the screen. 
It will not make it easy to read, so next exercise we will learn how to write 
this text to a .txt file.
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

def get_tag_elements(soup, tag):
    return soup.find_all(tag)

def get_paragraphs(soup, classes):
    paragraphs = []
    filter_paragraphs = []
    links = get_tag_elements(soup, 'p')
    
    for j in links:
        paragraphs.append(j)
    
    for i, p in enumerate(paragraphs):
        if i <= 5 or i >= len(paragraphs)-6:
            continue
        filter_paragraphs.append(p.text)
    return filter_paragraphs

if __name__ == "__main__":
    url = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'

    html = get_site(url)
    soup = beauty_site(html)

    article = ''.join(get_paragraphs(soup, 'p'))
    print(article)