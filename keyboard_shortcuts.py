from bs4 import BeautifulSoup as bs
import requests

hotkeys = 'https://mixxx.org/manual/2.2/en/chapters/appendix.html#keyboard-mapping-table'
response = requests.get(hotkeys)
raw_html = bs(response.content, 'html.parser')
print(raw_html)



#shortcuts = soup.findAll('a', {'title': 'title here'})
#print(shortcuts[0].text())