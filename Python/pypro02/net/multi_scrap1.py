'''
멀티 프로세싱을 통한 웹 스크랩핑 : multiprocessing X
(스크랩핑:1번만 긁어옴, 크롤링:주기적으로 긁어옴)
'''
import requests, time
from bs4 import BeautifulSoup as bs

def get_link():
    url = "https://beomi.github.io/beomi.github.io_old/"
    data = requests.get(url).text
    soup = bs(data, 'html.parser')
    #print(soup)
    my_title = soup.select('h3 > a')
    data = []
    
    for title in my_title:
        data.append(title.get('href'))
    
    return data

def get_content(link):
    head_link = 'https://beomi.github.io' + link
    data = requests.get(head_link).text
    soup = bs(data, 'html.parser')
    print(soup.select('h1')[0].text)
    

if __name__ == '__main__':
    start_time = time.time()
    
    for link in get_link():
        get_content(link)
    
    print('처리 시간 : %s초'%(time.time() - start_time))

#처리 시간 : 24.516031742095947초