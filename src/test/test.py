import requests
from bs4 import BeautifulSoup


def get_search_url(name='月亮与六便士'):
    s = requests.session()
    s.keep_alive = False
    url = 'https://www.zjkhuiyu.com/search.php?q=' + name
    response = s.get(url)
    search_soup = BeautifulSoup(response.text)
    item = search_soup.select_one('div[class="ans_list"] a')
    return item.get('href')


def get_article():
    url = get_search_url()
    response = requests.get(url)
    soup = BeautifulSoup(response.text)
    p_list = soup.select(
        '''div[id="wrap"] 
        div[class="wrap container"] 
        div[class="main"] 
        article 
        div[id="article-article"] 
        div[data-desc="article"] 
        p''')
    str = ''
    flag = False
    for item in p_list:
        txt = item.text.strip()
        if is_num_start(txt) and flag is False:
            flag = True
            str += txt + '\n'
        elif is_num_start(txt) is False and flag:
            str += item.text + '\n'
        elif is_num_start(txt) and flag:
            break
    return str


def is_num_start(str):
    return str[0] in '0123456789'


def get_article1(name):
    f = open('../resource/article/' + name + '.txt', encoding='utf-8')
    content = f.readline()
    while content:
        print(content)
        content = f.readline()


if __name__ == '__main__':
    message = '名句-圣经'
    arr = message.split('-')
    print(get_article1(arr[1]))
