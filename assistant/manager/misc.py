# blackstorm - UserBot
# Copyright (C) 2021 TeamBlackStorm
#
# This file is a part of < https://github.com/TeamBlackStorm/blackstorm/ >


import aiohttp

from . import *


@blackstorm_cmd(pattern="echo ?(.*)", type=["manager"])
async def oqha(e):
    match = e.pattern_match.group(1)
    if match:
        text = match
        reply_to = e
    elif e.is_reply:
        text = (await e.get_reply_message()).text
        reply_to = e.reply_to_msg_id
    else:
        return await eor(e, "What to Echo?", time=5)
    await e.client.send_message(e.chat_id, text, reply_to=reply_to)


@blackstorm_cmd(pattern="kickme$", type=["manager"], allow_all=True)
async def doit(e):
    if e.sender_id in DEVLIST:
        return await eod(e, "`I will Not Kick You, my Developer..`")
    try:
        await e.client.kick_participant(e.chat_id, e.sender_id)
    except Exception as Fe:
        return await eor(e, str(Fe), time=5)
    await eor(e, "Yes, You are right, get out.", time=5)


@blackstorm_cmd(pattern="joke$", type=["manager"])
async def do_joke(e):
    e = await e.get_reply_message() if e.is_reply else e
    link = "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&type=single"
    async with aiohttp.ClientSession() as ses:
        async with ses.get(link) as out:
            out = await out.json()
    await e.reply(out["joke"])
