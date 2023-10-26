try:
    import requests
    from bs4 import BeautifulSoup
except Exception as e:
    print('Modules Missing {}'.format(e))

file1 = open('../data/10entries.txt', 'r')

aggr = []

while True:
    url = file1.readline().strip()
    if url == "":
        break
    url = "https://github.com" + url
    print(url)

    try:
        r = requests.get(url)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, 'html.parser')
        date = soup.find('relative-time').get_text()
        # a = soup.find_all('div', class_="file-header d-flex flex-md-row flex-column flex-md-items-center file-header--expandable js-file-header js-skip-tagsearch")
        title = soup.find_all('a', class_="Link--primary Truncate-text")
        addDel = soup.find_all('span', class_="sr-only")

        title1 = []
        addDel1 = []

        addDel.pop(0)
        addDel.pop(0)

        for i in title:
            title1.append(i["title"])
        for i in addDel:
            addDel1.append(i.text)

        data = [title1, addDel1, date]
        aggr.append(data)

    except requests.exceptions.RequestException as e:
        print(f"Request error for {url}: {e}")
    except Exception as e:
        print(f"Error processing {url}: {e}")

for i in aggr:
    print(i)

file1.close()
