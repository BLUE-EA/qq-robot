import requests
from nonebot import on_keyword
from nonebot.adapters.onebot.v11 import Event, Bot, Message
from nonebot.typing import T_State

xljt = on_keyword({'心灵鸡汤', '心灵寄汤'})


@xljt.handle()
async def lj(bot: Bot, event: Event, state: T_State):
    lovelive_send = await xi()
    await xljt.finish(Message(f'[CQ:at,qq={event.get_user_id()}]' + lovelive_send))


async def xi():
    url = 'http://api.yanxi520.cn/api/xljtwr.php?charset=utf-8http://api.yanxi520.cn/api/xljtwr.php?encode=txt'
    hua = requests.get(url=url)
    data = hua.text
    return data
