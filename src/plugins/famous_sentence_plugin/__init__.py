import requests
from bs4 import BeautifulSoup
from nonebot import on_keyword
from nonebot.adapters.onebot.v11 import Event, Bot, Message
from nonebot.typing import T_State

keyword = on_keyword({'名句'})


def get_search_url(name='圣经'):
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
        div[id="article-content"] 
        div[data-desc="content"] 
        p''')
    str = ''
    flag = False
    for item in p_list:
        txt = item.text
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

@keyword.handle()
async def method(bot: Bot, event: Event, state: T_State):
    msg = get_article()
    await keyword.finish(Message(msg))
