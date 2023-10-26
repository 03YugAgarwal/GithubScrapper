try:
    import requests
    from bs4 import BeautifulSoup
except Exception as e:
    print('Modules Missing {}'.format(e))

file1 = open('../data/href.txt', 'r')
file2 = open('../data/commit_metrics.txt', 'w')

while True:
    url = file1.readline().strip()
    if url == "":
        break
    url = "https://github.com" + url
    print(url)

    try:
        r = requests.get(url)
        r.raise_for_status()  # Check if the request was successful
        soup = BeautifulSoup(r.text, 'html.parser')

        a = soup.find('div', class_='commit-title markdown-title').get_text()
        b = soup.find('div', class_='commit-desc').find('pre').get_text()

        c_container = soup.find('div', class_='d-flex flex-items-center js-details-container Details flex-1')
        c_elements = c_container.findAll('strong')
        c_texts = [element.get_text() for element in c_elements]
        c = "\n".join(c_texts)
        d = soup.find('relative-time').get_text()
        file2.write(a + "\n" + b + "\n" + c + "\n" + "DATE:"+d + "\n" + "-----------" + "\n")

    except requests.exceptions.RequestException as e:
        print(f"Request error for {url}: {e}")
    except Exception as e:
        print(f"Error processing {url}: {e}")

file1.close()
file2.close()