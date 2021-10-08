# blackstorm - UserBot
# Copyright (C) 2021 TeamBlackStorm
#
# This file is a part of < https://github.com/TeamBlackStorm/blackstorm/ >

import re

from . import *

STRINGS = {
    1: """🎇 **Thanks for Deploying blackstorm Userbot!**

• Here, are the Some Basic stuff from, where you can Know, about its Usage.""",
    2: """🎉** About blackstorm**

🧿 Blackstorm is Pluggable and powerful Telethon Userbot, made in Python from Scratch. It is Aimed to Increase Security along with Addition of Other Useful Features.

❣ Made by **@BlackStormOP**""",
    3: """**💡• FAQs •**

-> [Username Tracker](https://t.me/BlackstormOP/24)
-> [Keeping Custom Addons Repo](https://t.me/BlackStormOP/28)
-> [Disabling Deploy message](https://t.me/BlackStormOP/27)
-> [Setting up TimeZone](https://t.me/BlackStormOP/22)
-> [About Inline PmPermit](https://t.me/BlackStormOP/21)
-> [About Dual Mode](https://t.me/BlackStormOP/18)
-> [Custom Thumbnail](https://t.me/BlackStormOP/13)
-> [About FullSudo](https://t.me/BlackStormOP/11)
-> [Setting Up PmBot](https://t.me/BlackStormOP/2)
-> [Also Check](https://t.me/BlackStormOP/14)

**• To Know About Updates**
  - Join @BlackStormOP.""",
    4: f"""• `To Know All Available Commands`

  - `{HNDLR}help`
  - `{HNDLR}cmds`""",
    5: """• **For Any Other Query or Suggestion**
  - Move to **@BlackStormSupport**.

• Thanks for Reaching till END.""",
}


@callback(re.compile("initft_(\\d+)"))
async def init_depl(e):
    CURRENT = int(e.data_match.group(1))
    if CURRENT == 5:
        return await e.edit(
            STRINGS[5],
            buttons=Button.inline("<< Back", "initbk_" + str(4)),
            link_preview=False,
        )
    await e.edit(
        STRINGS[CURRENT],
        buttons=[
            Button.inline("<<", "initbk_" + str(CURRENT - 1)),
            Button.inline(">>", "initft_" + str(CURRENT + 1)),
        ],
        link_preview=False,
    )


@callback(re.compile("initbk_(\\d+)"))
async def ineiq(e):
    CURRENT = int(e.data_match.group(1))
    if CURRENT == 1:
        return await e.edit(
            STRINGS[1],
            buttons=Button.inline("Start Back >>", "initft_" + str(2)),
            link_preview=False,
        )
    await e.edit(
        STRINGS[CURRENT],
        buttons=[
            Button.inline("<<", "initbk_" + str(CURRENT - 1)),
            Button.inline(">>", "initft_" + str(CURRENT + 1)),
        ],
        link_preview=False,
    )
