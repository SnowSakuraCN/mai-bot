from nonebot import on_command
from nonebot.matcher import Matcher

help = on_command('help')

@help.handle()
async def send_help(matcher: Matcher):
    await matcher.send(message="QWQ")
