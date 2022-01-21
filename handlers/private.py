import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/e719f19bbeeb7f55e6202.jpg",
        caption=f"""**ʜᴇʟʟᴏ ɪ'ᴍ ᴀᴅᴠᴀɴᴄᴇ ᴍᴜsɪᴄ ʀᴏʙᴏᴛ ᴅᴇᴘʟᴏʏᴇᴅ ᴠᴘs  𝐬𝐚𝐧𝐭𝐡𝐮 𝐬𝐞𝐫𝐯𝐞𝐫💞. 
┏━━━━━━━━━━━━━━━━━┓
┣» ᴏᴘ ᴍᴜꜱɪᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ. 
┣» ʜɪɢʜ ǫᴜᴀʟɪᴛʏ  ᴍᴜꜱɪᴄ.
┣» ᴀᴅᴠᴀɴᴄᴇᴅ ꜰᴇᴀᴛᴜʀᴇꜱ.
┣» ꜱᴜᴘᴇʀꜰᴀꜱᴛ ꜱᴘᴇᴇᴅ.
┗━━━━━━━━━━━━━━━━━┛
[𝐒𝐚𝐧𝐭𝐡𝐮 ❤️](https://t.me/santhu_music_bot)



𝐈𝐟 𝐘𝐨𝐮 𝐇𝐚𝐯𝐞 𝐀𝐧𝐲 𝐐𝐮𝐞𝐬𝐭𝐢𝐨𝐧𝐬 𝐀𝐧𝐝 𝐇𝐞𝐥𝐩 𝐓𝐡𝐞𝐧 𝐃𝐦 𝐌𝐲 𝐁𝐨𝐬𝐬 = [𝐒𝐚𝐧𝐭𝐡𝐮 𝐁𝐨𝐭🐱❤️](https://t.me/santhu_music_bot)**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥀 𝐍𝐀𝐍𝐔 𝐆𝐑𝐎𝐔𝐏 𝐋𝐎 𝐀𝐃𝐃 𝐂𝐇𝐄𝐒𝐔 𝐊𝐎𝐍𝐃𝐈 ✨", url=f"https://t.me/{BOT_USERNAME}?startgroup=true", 
                ]
                
           ]
        ),
    )
    

@Client.on_message(command(["repo"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/e719f19bbeeb7f55e6202.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 𝐁𝐨𝐭'𝐬💞", url=f"https://telegra.ph/Santhosh-01-18")
                ]
            ]
        ),
    )
