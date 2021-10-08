# blackstorm - UserBot
# Copyright (C) 2021 TeamBlackStorm
#
# This file is a part of < https://github.com/TeamBlackStorm/blackstorm/ >

from . import *


@asst_cmd("ban")
@owner
async def banhammer(event):
    if not event.is_private:
        return
    x = await event.get_reply_message()
    if x is None:
        return await event.edit("Please reply to someone to ban him.")
    target = get_who(x.id)
    if is_blacklisted(target):
        return await asst.send_message(event.chat_id, "User is already banned!")

    blacklist_user(target)
    await asst.send_message(event.chat_id, f"#BAN\nUser - {target}")
    await asst.send_message(
        target,
        "`GoodBye! You have been banned.`\n**Further messages you send will not be forwarded.**",
    )


@asst_cmd("unban")
@owner
async def banhammer(event):
    if not event.is_private:
        return
    x = await event.get_reply_message()
    if x is None:
        return await event.edit("Please reply to someone to ban him.")
    target = get_who(x.id)
    if not is_blacklisted(target):
        return await asst.send_message(event.chat_id, "User was never banned!")

    rem_blacklist(target)
    await asst.send_message(event.chat_id, f"#UNBAN\nUser - {target}")
    await asst.send_message(target, "`Congrats! You have been unbanned.`")
