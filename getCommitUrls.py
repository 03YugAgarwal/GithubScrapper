try:
    import requests
    import csv
    from bs4 import BeautifulSoup
except Exception as e:
    print('Modules Missing {}'.format(e))
file1 = open('./next_link.txt', 'r')
file2 = open('./href.txt', 'w')
while (True):
    url = file1.readline()
    if (url == ""):
        break
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    a = soup.findAll('a', class_='Link--primary text-bold js-navigation-open markdown-title')

    href = set()
    for i in a:
        href.add(i['href'])

    for i in href:
        print(i)
        file2.write(i + "\n")
file1.close()
file2.close()
