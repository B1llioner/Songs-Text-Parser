from bs4 import BeautifulSoup
import requests

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'

HEADERS = {"user-agent" : USER_AGENT }

s_text = '''-----------------------------
Исполнитель {}
Текст песни {} :
{}
-----------------------------
'''

a = input("Исполнитель =>>> ")
b = input("Песня =>>> ")

base = "https://google.com/search?q={} {} текст".format(str(a), str(b))

def get_html(url, headers=HEADERS, params=''):
    r = requests.get(url, params=params)
    return r

a1 = get_html(base)

def get_content(html):
    soup = BeautifulSoup(html, 'lxml')
    return soup.prettify()

with open('html.html', 'w', encoding='utf-8') as file:
    file.write(str(get_content(a1.text)))

with open('html.html', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'lxml')

match = soup.find('div', class_='hwc')
match2 = match.div.div.div.text
match3 = match2[17:]

with open('song_text.txt', 'w') as file:
    file.write(s_text.format(str(a),str(b),str(match3)))

print(match3)