import asyncio
import os
from pyrogram.types import CallbackQuery
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
import requests
import pyrogram
from pyrogram import Client, emoji 
from config import *
from pyrogram import filters
from strings.filters import command
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified



@app.on_message(
    command(SZAQ_COMMAND_chh)
    & filters.channel
    & ~BANNED_USERS
async def cr_source(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/3123f5336cb10b95f6c0d.jpg",
        caption=f"""** 𝐒𝐎𝐔𝐑𝐂𝐄 𝐒𝐎𝐇𝐀**\nمرحبا بك عزيزي {message.from_user.mention}\nانا بوت ميوزك خاص بالقنوات \n لمعرفة الاوامر اضغط على زر الاوامر""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " الاوامر ", callback_data="usage"), 
                 ],[
                    InlineKeyboardButton(
                        "𓆩 |𓆩˹𓏺َِ •المطور", url=f"https://t.me/zxdrti"),
                 ],[
                
                    InlineKeyboardButton(
                        "★ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐒𝐎𝐇𝐀★ ", url=f"https://t.me/Mlze1bot"),
                ],

            ]

        ),

    )

    
@app.on_callback_query(filters.regex("usage"))
async def cr_usage(_, callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text(
        text="""**𝐒𝐎𝐔𝐑𝐂𝐄 𝐒𝐎𝐇𝐀**
★¦ اهلا بك عزيزي في قسم الأوامر
★¦ لتتمكن من تشغيل الميوزك بالقنوات فقط اكتب
★¦اكتب شغل + الاغنيه - للتشغيل آي اغنيه بالقناة 
★¦ اكتب تخطي- لتخطي الاغنيه 
★¦ اكتب انهاء- لانهاء التشغيل 
★¦ اكتب توقف- لايقاف التشغيل مؤقتا 
★¦اكتب واصل او استمر-  لاستمرار التشغيل 
                 **𝐒𝐎𝐔𝐑𝐂𝐄 𝐒𝐎𝐇𝐀**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𓆩 |𓆩˹𓏺َِ •المطور", url=f"https://t.me/zxdrti"), 
                ]
            ]
        )
    )

    
@app.on_callback_query(filters.regex("back"))
async def cr_back(_, callback_query: CallbackQuery):
    message = callback_query.message
  
    await message.edit_reply_markup(reply_markup=InlineKeyboardMarkup(
        
            [InlineKeyboardButton("طريقة الإستخدام", callback_data="usage")],
            [InlineKeyboardButton("|𓆩˹𓏺َِ •المطور", url=f"https://t.me/A_S_A_S_K")
             
            [InlineKeyboardButton("★ 𝐒𝐎𝐔𝐑𝐂𝐄•𝐒𝐎𝐇𝐀⚡", url=f"https://t.me/Mlze1bot")],
        ]
    ))
