import requests
from nonebot import require, get_bot

scheduler = require('nonebot_plugin_apscheduler').scheduler


def get_data():
    response = requests.get('http://bjb.yunwj.top/php/qq.php')
    data = response.text
    data_arr = data.split('【换行】')
    res = ''
    for i in range(1, data_arr.__len__() - 1):
        res += data_arr[i] + '\n'
    return res


@scheduler.scheduled_job('cron', hour=17, minute=0)
async def demo():
    bot = get_bot('2381186949')
    group_id = 713325058
    message = get_data()
    await bot.send_group_msg(group_id=group_id, message=message)
