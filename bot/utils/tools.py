import base64
import json
import re

import requests
from pyrogram.errors import ChatAdminRequired, ChatWriteForbidden, UserNotParticipant
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot.utils.config import (
    LOG_CHANNEL,
    MAIN_CHANNEL,
    MAIN_CHANNEL_2,
    MAIN_CHANNEL_3,
    MAIN_CHANNEL_4,
    MAIN_CHANNEL_5,
    DOUBLE_SHORT,
    DOUBLE_SHORT_API,
    DOUBLE_SHORT_WEB,
    ORIGINAL_LINK,
)
from bot.utils.database import db
from bot.utils.logger import Logger


class Base64:
    def decode(base64_string):
        base64_bytes = base64_string.encode("ascii")
        string_bytes = base64.b64decode(base64_bytes)
        string = string_bytes.decode("ascii")
        return string

    def encode(string):
        string_bytes = string.encode("ascii")
        base64_bytes = base64.b64encode(string_bytes)
        base64_string = base64_bytes.decode("ascii")
        return base64_string


def shorten_url(api: dict, url: str):
    api_key = api["key"]
    api_url = api["url"]
    api_url = api_url.format(api_key, url)
    try:
        response = requests.get(api_url)
        if response.ok:
            data = json.loads(response.text)
            short_url = data[get_keydata(api_url)]
            if DOUBLE_SHORT:
                double_api = DOUBLE_SHORT_WEB.format(DOUBLE_SHORT_API, short_url)
                resp2 = requests.get(double_api)
                if resp2.ok:
                    data2 = json.loads(resp2.text)
                    doubled = data2[get_keydata(double_api)]
                    return doubled
                else:
                    return short_url
            else:
                return short_url
        else:
            return None
    except Exception as e:
        Logger.exception(e)
        return None


def get_keydata(api_url):
    _list = api_url.split("/")
    api_site = _list[2]
    if api_site == "api.shareus.in":
        return "shortlink"
    else:
        return "shortenedUrl"


def check_url(url):
    url_pattern = re.compile(r"^https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+")
    if url_pattern.match(url):
        return True
    else:
        return False


async def make_short_url(m, api: dict, url: str, edit: bool = False):
    api_key = api["key"]
    api_web = api["url"]
    if not api_key and not api_web:
        if edit:
            return await m.edit_text(
                "**Seems Like There is Some Issue. Contact @NORMAN_2_2_1_9_4**"
            )
        else:
            return await m.reply_text(
                "**Seems Like There is Some Issue. Contact @NORMAN_2_2_1_9_4**"
            )

    if not check_url(url):
        if edit:
            return await m.edit_text(
                "**Seems Like There is Some Issue. Contact @NORMAN_2_2_1_9_4**"
            )
        else:
            return await m.reply_text(
                "**Seems Like There is Some Issue. Contact @NORMAN_2_2_1_9_4**"
            )

    if ORIGINAL_LINK:
        short_url = url
    else:
        short_url = shorten_url(api, url)

    # send link to user
    send_btn = [
        [InlineKeyboardButton("𝗝𝗼𝗶𝗻 𝗙𝗶𝗹𝗲𝘀 𝗕𝗮𝗰𝗸𝘂𝗽 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url="https://t.me/+ZXHf4aROwNdiODg9")],
        [InlineKeyboardButton("𝗢𝗽𝗲𝗻 𝗟𝗶𝗻𝗸", url=short_url)],
    ]

    if edit:
        try:
            await m.edit_text(
                text="<b><i>» Here is Your Requested Link, Click The ''<u>Open Link</u>'' Button Below. \n\n» How To Open? - <a href='https://t.me/Sonic_Club/144'>Watch Tutorial</a> \n\n» Any Other Issues Like 'Username Not Found' <a href='https://t.me/HAnime_Club/233'>Click Here</a> \n\n» Must Send Join Request To <a href='https://t.me/+ZXHf4aROwNdiODg9'>𝗙𝗶𝗹𝗲𝘀 𝗕𝗮𝗰𝗸𝘂𝗽 𝗖𝗵𝗮𝗻𝗻𝗲𝗹</a> To Access All The Files.</i></b>",
                reply_markup=InlineKeyboardMarkup(send_btn),
                disable_web_page_preview=True,
            )
        except Exception as e:
            Logger.info(f"[make_short_url edit]: {e}")
    else:
        try:
            await m.reply_text(
                text="<b><i>» Here is Your Requested Link, Click The ''<u>Open Link</u>'' Button Below. \n\n» How To Open? - <a href='https://t.me/Sonic_Club/144'>Watch Tutorial</a> \n\n» Any Other Issues Like 'Username Not Found' <a href='https://t.me/HAnime_Club/233'>Click Here</a> \n\n» Must Send Join Request To <a href='https://t.me/+ZXHf4aROwNdiODg9'>𝗙𝗶𝗹𝗲𝘀 𝗕𝗮𝗰𝗸𝘂𝗽 𝗖𝗵𝗮𝗻𝗻𝗲𝗹</a> To Access All The Files.</i></b>",
                reply_markup=InlineKeyboardMarkup(send_btn),
                disable_web_page_preview=True,
            )
        except Exception as e:
            Logger.info(f"[make_short_url non-edit]: {e}")


async def check_user(client, msg, bot_id: int):
    chat_id = msg.from_user.id
    if not await db.is_user_exist(chat_id, bot_id):
        data = await client.get_me()
        BOT_USERNAME = data.username
        await db.add_user(chat_id, bot_id)
        if LOG_CHANNEL:
            await client.send_message(
                LOG_CHANNEL,
                f"#NEWUSER: \n\nNew User [{msg.from_user.first_name}](tg://user?id={msg.from_user.id}) started @{BOT_USERNAME} !!",
            )
        else:
            Logger.info(
                f"#NewUser: \n\nName: {msg.from_user.first_name} \nID: {msg.from_user.id}"
            )

    await msg.continue_propagation()


chan = {
    1: MAIN_CHANNEL,
    2: MAIN_CHANNEL_2,
    3: MAIN_CHANNEL_3,
    4: MAIN_CHANNEL_4,
    5: MAIN_CHANNEL_5,
}


async def forcesub(app, msg, channel: int, data=False, cb=False):
    ch_join = False
    channel_name = chan[channel]
    ch_info = await app.get_chat(channel_name)
    ch_link = f"https://t.me/{ch_info.username}"
    ch_title = ch_info.title
    ch_id = ch_info.id

    try:
        try:
            await app.get_chat_member(ch_id, msg.from_user.id)
        except UserNotParticipant:
            ch_join = True

        if ch_join:
            try:
                if cb:
                    await cb.answer(
                        "You have not yet joined my channel.", show_alert=True
                    )
                    return
                if data:
                    buttons = [
                        [InlineKeyboardButton(f"Join {ch_title}", url=ch_link)],
                        [InlineKeyboardButton("Join Backup", url="https://t.me/+oIjQyg8ek3FhNzA1")],
                        [InlineKeyboardButton("Try Again", f"retry#{data}#{channel}")],
                    ]
                else:
                    buttons = [
                        [InlineKeyboardButton(f"• Join {ch_title} •", url=ch_link)],
                    ]
                await msg.reply(
                    "**You Have Not Joined My Channel Yet. Please Join Both By Clicking The Button Below**",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup(buttons),
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
            return True
    except ChatAdminRequired:
        print(f"I'm not admin in the chat: @{MAIN_CHANNEL} !")
    return False


async def aexec(code, client, message):
    exec(
        "async def __aexec(client, message): "
        + "".join(f"\n {l_}" for l_ in code.split("\n"))
    )
    return await locals()["__aexec"](client, message)
