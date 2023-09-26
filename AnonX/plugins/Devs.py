import asyncio
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AnonX import app, Telegram
import random
@app.on_message(
    command(["سهى","سورررس","السورس","سورس", "crs"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/e549ba4defc831d5c5d35.jpg",
        caption=f"""
 [𝐒𝐎𝐔𝐑𝐂𝐄•𝐒𝐎𝐇𝐀](https://t.me/Mlze1bot)
 —————————————
 [𝐒𝐎𝐇𝐀  𓅉](https://t.me/Mlze1bot)
 
 [𓏺𝙂𝙍𝙊𝙐𝙋 𝙃𝞝𝙇𝙋](https://t.me/ASAAQLIO)
  
 [⍟𓏺𝙒𝞝𝙇𝘾𝙊𝙈𝙀 𝙏𝙊 𝐒𝐎𝐔𝐑𝐂𝐄•𝐒𝐎𝐇𝐀](https://t.me/ASAAQLIO)
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝐂𝐑𝐘𝐒𝐓𝐀𝐋", url=f"https://t.me/Mlze1bot"), 
                ],[
                    InlineKeyboardButton(
                        "𝐒𝐎𝐔𝐑𝐂𝐄•𝐒𝐎𝐇𝐀", url=f"t.me/ASAAQLIO"),
                ],

            ]

        ),

    )

@app.on_message(command([f"غنيلي", "غني", "غ", "{BOT_USERNAME} غنيلي"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(8,20)
    url = f"https://t.me/iV_P_Nl/{rl}"
    await client.send_voice(message.chat.id,url,caption="`🔥 ¦ تـم اختيـار الاغـنـية لـك`",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )
    
@app.on_message(command(["صورة","صور"]))
async def ihd(client: Client, message: Message):
    rs = random.randint(39,148)
    url = f"https://t.me/GTTUTY/{rs}"
    await client.send_photo(message.chat.id,url,caption="`💕 ¦ تـم اختيـار الصوره لـك`",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )

                        


