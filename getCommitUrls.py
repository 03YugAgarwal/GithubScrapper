try:
    import requests
    from bs4 import BeautifulSoup
except Exception as e:
    print('Modules Missing {}'.format(e))

url = "https://github.com/apache/dubbo/commits/3.2"

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

a = soup.findAll('a', class_='Link--primary text-bold js-navigation-open markdown-title')

href = set()
for i in a:
    href.add(i['href'])

for i in href:
    print(i)
