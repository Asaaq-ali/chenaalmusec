import asyncio

import os
import time
import requests
from config import USER_OWNER, OWNER_ID, SUPPORT_CHANNEL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
from random import  choice, randint

                
@app.on_message(
    command(["مطورين ا","المطورين","مطورين","مطورين سهى"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/6ae4c163aac6f69ad9eb9.jpg",
        caption=f"""*𝐒𝐎𝐔𝐑𝐂𝐄•𝐒𝐎𝐇𝐀**\nمرحبا بك عزيزي {message.from_user.mention} في قسم مطورين سهى ميوزك\nللتحدث مع مطورين اضغط علي الازرار بالاسفل👇\n**𝐒𝐎𝐔𝐑𝐂𝐄•𝐒𝐎𝐇𝐀**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒•𝐒𝐎𝐇𝐀 ˹َّّ ", url=f"https://t.me/smauabot"), 
                 ],[
                    
                
                    InlineKeyboardButton(
                        "𓏺𝙒𝙃𝙄𝙎𝙆𓏺𝞝𝙔", url=f"https://t.me/A_S_A_S_K"),
                ],[
                    
                
                    InlineKeyboardButton(
                        "★𝐒𝐎𝐔𝐑𝐂𝐄•𝐒𝐎𝐇𝐀⚡", url=f"https://t.me/Mlze1bot"),
                
        ],

            ]

        ),

    )










@app.on_message(
   command(["مبرمج السورس","المبرمج"])
   
)
async def yas(client, message):
    usr = await client.get_chat("A_S_A_S_K")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⌞𝐒𝐎𝐔𝐑𝐂𝐄•𝐒𝐎𝐇𝐀\nمعلومات مبرمج السورس \n↜︙Dev Name ↬ :{name} \n↜︙Dev User ↬ :@{usr.username} \n↜︙Dev id ↬ :{usr.id}**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],  [
                    InlineKeyboardButton(
                        "استدعاء المبرمج", url=f"https://t.me/{usr.username}"),                        
                 ],
            ]
        ),
    )


@app.on_message(
  command(["المطور"])
  
)
async def yas(client, message):
    usr = await client.get_chat(USER_OWNER)
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⌞𝐒𝐎𝐔𝐑𝐂𝐄•𝐒𝐎𝐇𝐀 \nمعلومات المطور الاساسي\n↜︙Dev Name ↬ :{name} \n↜︙Dev User ↬ :@{usr.username} \n↜︙Dev id ↬ :{usr.id}**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],   [
                    InlineKeyboardButton(
                        "استدعاء المطور", url=f"https://t.me/{usr.username}"),                        
                 ],
                      [
                    InlineKeyboardButton(
                        "قناة المطور", url=f"https://t.me/{SUPPORT_CHANNEL}"),                        
                 ],
            ]
        ),
    )
@app.on_message(
   command(["قناة المطور"])
   
)
async def yas(client, message):
    usr = await client.get_chat(SUPPORT_CHANNEL)
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**قناة المطور \nاشترك فالقناه فضلا وليس امرا من الازرار في الاسفل \n\n رابط القناه: : https://t.me/{usr.username}**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ], 
            ]
        ),
    )



@app.on_message(
   command(["ذكاء اصتناعي"])
   
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/2d3ae472e923d61ce3504.jpg",
        caption=f"""**𝐒𝐎𝐔𝐑𝐂𝐄•𝐒𝐎𝐇𝐀**\nمرحبا بك عزيزي {message.from_user.mention} في قسم الذكاء الاصتناعي الخاص بسورس سهۍ\nلتتمكن من استخدام اوامر الذكاء الاصتناعي اكتب \n سؤال + السؤال بالاسفل 👇\n**𝐒𝐎𝐔𝐑𝐂𝐄•𝐒𝐎𝐇𝐀**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒•𝐂𝐑𝐘𝐒𝐓𝐀𝐋 ˹َّّ", url=f"https://t.me/A_S_A_S_K"), 
                 ],[
                
                    InlineKeyboardButton(
                        "★𝐒𝐎𝐔𝐑𝐂𝐄•𝐒𝐎𝐇𝐀⚡", url=f"https://t.me/Mlze1bot"),
                ],

            ]

        ),

    )



@app.on_message(
   command(["قرأن"])
   
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/2d3ae472e923d61ce3504.jpg",
        caption=f"""**𝐒𝐎𝐔𝐑𝐂𝐄•𝐒𝐎𝐇𝐀**\nمرحبا بك عزيزي {message.from_user.mention} في قسم تشغيل القرأن الخاص بسورس سهۍ\nلتتمكن من استخدام اوامر القرأن اكتب \n سورة + اسم السورة بالاسفل👇\n**𝐒𝐎𝐔𝐑𝐂𝐄•𝐒𝐎𝐇𝐀**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒•𝐂𝐑𝐘𝐒𝐓𝐀𝐋 ˹َّّ", url=f"https://t.me/A_S_A_S_K"), 
                 ],[
                
                    InlineKeyboardButton(
                        "★𝐒𝐎𝐔𝐑𝐂𝐄•𝐒𝐎𝐇𝐀⚡", url=f"https://t.me/Mlze1bot"),
                ],

            ]

        ),

    )

    
