import requests
from bs4 import BeautifulSoup
import json


URL = "https://github.com/apache/kafka"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
links = []

result = soup.find_all('a', class_="js-navigation-open Link--primary")

for i in result:
    links.append("https://github.com" + i["href"])

while len(links) > 0:
    print(links[0])
    page = requests.get(links[0])
    soup = BeautifulSoup(page.content, "html.parser")

    y = json.loads(soup.text)

    if "payload" in y:
        payload = y["payload"]
        if "tree" in payload:
            tree = payload["tree"]
            if "items" in tree:
                arr = tree["items"]

        for i in arr:
            links.append("https://github.com/apache/kafka/tree/trunk/" + i["path"])

    links.pop(0)
