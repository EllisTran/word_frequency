from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import re
from collections import Counter
import string
import json


def search(url, filename, num):
    counts = dict()
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    web_byte = urlopen(req).read()
    webpage = web_byte.decode('utf-8')
    all_text = ''
    soup = BeautifulSoup(webpage, 'html.parser')
    for p in soup.findAll('p'):
        all_text += p.getText()

    all_text = all_text.translate(str.maketrans('', '', string.punctuation))
    words = all_text.split()
    d = {' '.join(words):n for words,n in eval(counter_appender(num)) if not  words[0][-1]==(',')} 
    d = sorted(d.items(), key=lambda x: x[1], reverse=True)


    f = open(filename, "w")
    f.write("This is for the article %s\n"%(url))
    for word, freq in d:
        f.write("% s % s\n"%(word, freq))

def counter_appender(num):
    str = "Counter(zip(words,"
    for i in range(num-1):
        if i == num-2:
            str = str + "words[%s:]"%(i+1)
        else:
            str = str + "words[%s:],"%(i+1)
    return str+')).items()'


def start_program():
    num = int(input("Enter the type of word frequency you would like. \nEX: 2 would give 'enviornmental science'. 3 would give 'the life of'. 4 'i love peanut butter' \n"))

    article_url = str(input('Now enter the url of the article!\n'))

    file_name = str(input("Input name of file you want to save to\n"))
    file_name = file_name + '.txt'
    search(article_url, file_name, num)

start_program()