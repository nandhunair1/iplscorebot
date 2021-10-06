"""
    IPL Score Telegram Bot
    Copyright (C) 2021 @ImJanindu

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import os
import logging
from bs4 import BeautifulSoup
import requests
from pyrogram import Client, filters, idle
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from vars import API_ID, API_HASH, BOT_TOKEN

bot = Client(
    "iplscore",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@bot.on_message(filters.private & filters.command("start"))
async def score(_, message):
    m = await message.reply_text("`Gathering ongoing ipl match scorecard...`")
    try:       
        url = "https://www.espncricinfo.com/live-cricket-score"
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        
        match_descrition = soup.select(".description")
        obj1 = soup.select(".teams")
        status = soup.select(".status-text")
        text = ""
        text = text + match_descrition[1].text + "\n\n" + obj1[0].text + "\n\n" + status[0].text + "\n\n" + status[1].text + "\n\n" + "**Bot by @Infinity_Bots**"
        text = text.replace("eS", "e vs S")
        await m.edit(text, reply_markup=InlineKeyboardMarkup(
                                [[InlineKeyboardButton(
                                     "Refresh 🔁", url="https://t.me/iplscorerobot?start=true")]]))
        return
    except Exception as e:
        print(str(e))
        return await m.edit("`No any ongoing ipl matches at this time.`")


bot.start()
idle()
