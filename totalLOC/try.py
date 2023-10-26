import requests
from bs4 import BeautifulSoup
import json

URL = "https://github.com/apache/dubbo/commit/711de7c2a0f8ca01b3f0e7ef5a8e96495a10bb0a"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

a = soup.find('div', class_="file-header d-flex flex-md-row flex-column flex-md-items-center file-header--expandable js-file-header js-skip-tagsearch")

print(a)

# y = json.loads(soup.text)
#
# # Check if the "payload" key exists
#
# print(y)
#
# if "payload" in y:
#     payload = y["payload"]
#     if "tree" in payload:
#         tree = payload["tree"]
#         if "items" in tree:
#             arr = tree["items"]
#             print(arr)
