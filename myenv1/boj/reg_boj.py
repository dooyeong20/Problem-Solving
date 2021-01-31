import requests
from bs4 import BeautifulSoup
import os.path

title = ''
badge = ''
no = input('번호 : ')
webpage = requests.get("https://solved.ac/search?query=" + no)
soup = BeautifulSoup(webpage.content, "html.parser")

nos = soup.select('div.sticky-table-cell > span > .ProblemInline__ProblemStyle-cvf1lm-0 > span')
badges = soup.select('div.sticky-table-cell > span > .ProblemInline__ProblemStyle-cvf1lm-0 > img')
titles = soup.select('div.sticky-table-cell > span > a.hover_underline')

for i in range(len(nos)):
    if nos[i].get_text() == str(no):
        title = titles[i].get_text()
        badge = badges[i]['src']
        break

print(no + title + badge)
content = '<img height="25px" width="25px=" src="' +  badge + '"/>' + title

file_path = 'README.md'

f = open(file_path, "a", encoding='utf8')
f.write('\n')
f.write(content)
f.close()
print('Done !')