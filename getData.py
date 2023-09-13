try:
    import requests
    from bs4 import BeautifulSoup
except Exception as e:
    print('Modules Missing {}'.format(e))

url = "https://github.com/apache/dubbo/commit/8a509e9601fab4af278859c9d947fca8f5f0fa27"

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

a = soup.find('div', class_='commit-title markdown-title')
print(a)
b = soup.find('div', class_='commit-desc')
b = b.find('pre')
print(b)
c = soup.find('div', class_='d-flex flex-items-center js-details-container Details flex-1')
c = c.findAll('strong')
print(c)