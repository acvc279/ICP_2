from bs4 import BeautifulSoup
import requests
wiki_pagelink = requests.get("https://en.wikipedia.org/wiki/Deep_learning")
s = BeautifulSoup(wiki_pagelink.content, "html.parser")
print(s.title)
file = open("wiki.txt", "a+")
for link in s.find_all('a'):
    file.write("\n")
    file.write(str(link.get('href')))
file.close()