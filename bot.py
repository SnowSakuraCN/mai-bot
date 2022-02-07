#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import defaultdict

import nonebot
from nonebot.adapters.onebot.v11 import Adapter

nonebot.init()

app = nonebot.get_asgi()

driver = nonebot.get_driver()
driver.register_adapter(Adapter)

nonebot.load_plugins("src/plugins")
#nonebot.load_all_plugins([],"src/plugins")

if __name__ == "__main__":
    nonebot.run(app="bot:app")
