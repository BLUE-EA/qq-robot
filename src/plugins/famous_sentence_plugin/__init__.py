import random

from nonebot import on_keyword
from nonebot.adapters.onebot.v11 import Event, Bot, Message
from nonebot.typing import T_State

keyword = on_keyword({'#'})

books = ['原神', '三国演义']


def get_article(name):
    try:
        f = open('src/resource/article/' + name + '.txt', encoding='utf-8')
        arr = list()
        content = f.readline()
        while content:
            arr.append(content)
            content = f.readline()
        length = arr.__len__()
        rand = random.randint(0, length - 1)
        if name not in books:
            return arr[rand] + f'  ——《{name}》'
        else:
            return arr[rand]
    except Exception as e:
        print(e.__str__())
        return '该书籍未收录，请联系BLUE-EA'


@keyword.handle()
async def method(bot: Bot, event: Event, state: T_State):
    message = event.get_message().__str__()
    arr = message.split('#')
    if arr.__len__() <= 1:
        name = ''
    else:
        name = arr[1]
    if name is None or name == '':
        msg = '请输入书名，以“#书名”的格式写'
    else:
        msg = get_article(name)
    await keyword.finish(Message(msg))
