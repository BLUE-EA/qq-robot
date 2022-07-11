from nonebot import on_keyword
from nonebot.adapters.onebot.v11 import Event, Bot, Message
from nonebot.typing import T_State

msg = '''
    1、多屏幕划水，只要你熟悉掌握快捷键，老板就追不上你。（WIN键+→可以切换下一个屏幕）

　　2、在和办公室同事聊天的时候拿着笔和本子。

　　3、废文件不要扔，堆在桌子上，这样不但看起来很忙，而且能随时把手机藏起来。

　　4、带薪上厕所，最好的是配合茶水间使用，闲来没事就去接个水，所以你要准备最小的水杯，每次接最少的水。

　　5、不要用公司提供的网络上网，尤其是如果你上网需要通过客户端的话，那你的聊天记录、浏览记录都是可以看到的。

　　6、要有两个微信，一个摸鱼，一个上班。所以最好你的手机上，要装两个微信，要有两套朋友圈。

　　7、配备无线耳机，最好只戴一耳，一方面显得你业务繁忙，随时可能打电话，另一方面，你要是在听点什么，别人也不知道。。

　　8、假装和同事对接业务，花2分钟把该对接的事情说完，然后天南海北的胡扯，聊的越火热，越能给人热心工作，有团队意识的感觉。
'''

keyword = on_keyword({'摸鱼', '摸鱼技巧'})


@keyword.handle()
async def lj(bot: Bot, event: Event, state: T_State):
    await keyword.finish(Message(msg))
