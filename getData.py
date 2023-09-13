try:
    import requests
    from bs4 import BeautifulSoup
except Exception as e:
    print('Modules Missing {}'.format(e))
file1=open('./href.txt','r')
file2=open('./commit_metrics.txt','w')
#url = "https://github.com/apache/dubbo/commit/8a509e9601fab4af278859c9d947fca8f5f0fa27"
while(True):
    url=file1.readline()
    if(url==""):
        break
    url="https://github.com"+url
    print(url)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    a = soup.find('div', class_='commit-title markdown-title')
    print(a)
    b = soup.find('div', class_='commit-desc')
    b = b.find()
    print(b)
    c = soup.find('div', class_='d-flex flex-items-center js-details-container Details flex-1')
    c = c.findAll('strong')
    print(c)
    file2.write(a+"\n"+b+"\n"+c+"\n")
file1.close()
file2.close()