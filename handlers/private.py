import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgQAAxkBAAIDYGIKNVVcTDS2-ra3DLlMQ6jkGBigAAKACwACwsDYUXEHwEyrFM6hIwQ")
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/28f95b221efbefede9988.jpg",
        caption=f"""**━━━━━━━━━━━━ 🌺🌻🌹🌷━━━━━━━━━━
💟 [{BOT_NAME}](https://t.me/{BOT_USERNAME}) **ɴᴇɴᴜ ᴍᴏsᴛ ᴀᴅᴠᴀɴᴄᴇᴅ ᴍᴜsɪᴄ ᴍᴜsɪᴄ ʙᴏᴛ ɴɪ 💚 ɴᴀɴᴜ ɢʀᴏᴜᴘ ʟᴏ ᴀᴅᴅ ᴄʜᴇsᴜᴋᴏɴᴅɪ ᴍᴀɴᴄʜɪ ᴀᴜᴅɪᴏ ʙᴏᴛ ɴɪ 💘. 😁 ɴᴀɴᴜ ᴅᴇᴘʟᴏʏ ᴄʜᴇsɪɴᴀ ᴇᴅʜᴀᴠᴀ [sᴀɴᴛʜᴜ 💓](https://t.me/santhu_music_bot)
                                   
𝐈𝐟 𝐘𝐨𝐮 𝐇𝐚𝐯𝐞 𝐀𝐧𝐲 𝐐𝐮𝐞𝐬𝐭𝐢𝐨𝐧𝐬 𝐀𝐧𝐝 𝐇𝐞𝐥𝐩 𝐓𝐡𝐞𝐧 𝐃𝐦 𝐌𝐲 𝐁𝐨𝐬𝐬 = [𝐒𝐀𝐍𝐓𝐇𝐔❤️](https://t.me/santhu_music_bot)
━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔰sᴀɴᴛʜᴜ ɴɪ ᴀᴅᴅ ᴄʜᴇsᴜᴋᴏɴᴅɪ🔰", url="https://t.me/@Santhuoficialbot?startgroup=true")
                  ],[
                    InlineKeyboardButton(
                        "❤ᴏᴡɴᴇʀ🤎", url="https://t.me/santhu_music_bot"
                    ),
                    InlineKeyboardButton(
                        "💘ɢʀᴏᴜᴘ💞", url="https://t.me/santhuvc"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "💛ɴᴇᴛᴡᴏʀᴋ💚", url="https://t.me/santhubotupadates"
                    )]
            ]
       ),
    )

@Client.on_message(command(["cmd"]) & filters.group & ~filters.edited & ~filters.private)

async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4d30d32278a805efaa0b4.jpg",
        caption=f"""ᴄᴏᴍᴍᴀɴᴅs 💝""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💕ᴄᴏᴍᴍᴀɴᴅs ᴇxᴘʟᴀɴᴀᴛɪᴏɴ💕", url=f"https://telegra.ph/SANTHU-BOT-COMMANDS-02-14")
                ]
            ]
        ),
    )
