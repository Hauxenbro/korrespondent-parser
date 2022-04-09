import lxml.etree
import requests
from lxml import etree

def parse_art(url_art):
    banned_symb = """!@#$%^&~~[]/><'"_"""
    page = requests.get(url_art)
    root = etree.fromstring(page.text, parser)
    for i in root.iter('h1'):
        if 'class' in i.attrib:
            if i.attrib['class'] == 'post-item__title':
                art_name = i.text
    for char in art_name:
        if char in banned_symb:
            art_name = art_name.replace(char, '')

    for i in root.iter('div'):
        if 'class' in i.attrib:
            if i.attrib['class'] == 'post-item__text':
                part_art = i
    print('loading...')
    with open(art_name + '.txt', 'w', encoding = 'utf-8') as article_page:
        for i in part_art:
            if (i.tag.startswith('p') or i.tag.startswith('h')) and i.text is not None:
                if i.text.startswith('Новости от'):
                    break
                else:
                    article_page.write(i.text)
                    for j in i:
                        if j.text is not None:
                            if j.text.startswith('Новости от'):
                                break
                            else:
                                article_page.write(j.text)




url = 'https://korrespondent.net/'
res = requests.get(url)
parser = etree.HTMLParser()
root = etree.fromstring(res.text, parser)

for i in root.iter('div'):
    if 'class' in i.attrib:
        if i.attrib['class'] == 'time-articles':
            articles = i
            break
for i in articles.iter('a'):
    if 'href' in i.attrib:
        if i.attrib['href'].startswith('htt'):
            parse_art(str(i.attrib['href']))

