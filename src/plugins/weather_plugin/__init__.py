import urllib.parse

from nonebot import on_keyword
from nonebot.adapters.onebot.v11 import Event, Bot
from nonebot.adapters.onebot.v11.message import MessageSegment
from selenium import webdriver

keyword = on_keyword({'天气'})


@keyword.handle()
async def handle(bot: Bot, event: Event):
    mesg = event.get_message().__str__()
    image = get_weather(mesg)
    await keyword.send(MessageSegment.image(image))


def get_weather(city='广东广州天气'):
    brower = webdriver.PhantomJS()
    city = urllib.parse.quote(city)
    url = f"https://weathernew.pae.baidu.com/weathernew/pc?query={city}&srcid=4982"
    brower.get(url)
    brower.maximize_window()
    image = brower.get_screenshot_as_png()
    brower.close()
    return image
