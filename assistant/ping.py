# blackstorm - UserBot
# Copyright (C) 2021 TeamBlackStorm
#
# This file is a part of < https://github.com/TeamBlackStorm/blackstorm/ >

from datetime import datetime


@asst_cmd("ping$")
@owner
async def _(event):
    start = datetime.now()
    msg = await event.reply("Pong!")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await msg.edit(f"**Pong!!**\n `{ms} ms`")
