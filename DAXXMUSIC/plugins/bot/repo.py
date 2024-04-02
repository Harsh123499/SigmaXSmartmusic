from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from DAXXMUSIC import app
from config import BOT_USERNAME
from DAXXMUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """**
✪ ωεℓ¢σмє ƒσя 𝙷𝚊𝚛𝚜𝚑 яєρσѕ ✪
 
 ➲ ᴀʟʟ ʀᴇᴘᴏ ᴇᴀsɪʟʏ ᴅᴇᴘʟᴏʏ ᴏɴ ʜᴇʀᴏᴋᴜ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴇʀʀᴏʀ ✰
 
 ➲ ɴᴏ ʜᴇʀᴏᴋᴜ ʙᴀɴ ɪssᴜᴇ ✰
 
 ➲ ɴᴏ ɪᴅ ʙᴀɴ ɪssᴜᴇ ✰
 
 ➲ᴜɴʟɪᴍɪᴛᴇᴅ ᴅʏɴᴏs ✰
 
 ➲ ʀᴜɴ 24x7 ʟᴀɢ ғʀᴇᴇ ᴡɪᴛʜᴏᴜᴛ sᴛᴏᴘ ✰
 
 ► ɪғ ʏᴏᴜ ғᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴛʜᴇɴ sᴇɴᴅ ss
**"""




@app.on_message(filters.command("Lundlegakya"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝐀𝐃𝐃 𝐌𝐄", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("𝐇𝐄𝐋𝐏", url="https://t.me/HEROKUFREECC"),
          InlineKeyboardButton("𝐎𝐖𝐍𝐄𝐑", url="https://t.me/mr_harsh_zs2"),
          ],
               [
                InlineKeyboardButton("𝐋𝐈𝐕𝐄 𝐂𝐂", url="https://t.me/ALLTYPECC"),

],
[
              InlineKeyboardButton("𝐁𝐀𝐍 𝐀𝐋𝐋", url=f"https://github.com/DAXXTEAM/DAXXBANALL"),
              InlineKeyboardButton("︎𝐌𝐔𝐒𝐈𝐂", url=f"https://github.com/DAXXTEAM/DAXXMUSIC"),
              ],
              [
              InlineKeyboardButton("𝐌𝐀𝐍𝐀𝐆𝐄𝐌𝐄𝐍𝐓", url=f"https://github.com/DAXXTEAM/YumikooRobot"),
InlineKeyboardButton("𝐂𝐇𝐀𝐓 𝐁𝐎𝐓", url=f"https://github.com/DAXXTEAM/DAXXCHATBOT"),
],
[
InlineKeyboardButton("𝐒𝐓𝐑𝐈𝐍𝐆𝐁𝐎𝐓", url=f"https://github.com/DAXXTEAM/DAXXSTRINGBOT"),
InlineKeyboardButton("𝐂𝐇𝐀𝐓𝐆𝐏𝐓", url=f"https://github.com/DAXXTEAM/DAXXCHATGPT"),
],
[
              InlineKeyboardButton("𝐕𝐎𝐒", url=f"https://github.com/DAXXTEAM/Kaali-Linux"),
              InlineKeyboardButton("𝐌𝐎𝐕𝐈𝐄", url=f"https://github.com/DAXXTEAM/DAXXMOVIEBOT"),
              ],
              [
              InlineKeyboardButton("𝐒𝐓𝐑𝐈𝐍𝐆 𝐇𝐀𝐂𝐊", url=f"https://github.com/DAXXTEAM/DAXXSTRINGHACK"),
InlineKeyboardButton("𝐈𝐃 𝐂𝐇𝐀𝐓 𝐁𝐎𝐓", url=f"https://github.com/DAXXTEAM/DAXXIDCHAT"),
],
[
InlineKeyboardButton("𝐔𝐒𝐄𝐑𝐁𝐎𝐓", url=f"https://github.com/DAXXTEAM/DAXXUSERBOT"),
InlineKeyboardButton("𝐒𝐄𝐀𝐑𝐂𝐇𝐁𝐎𝐓", url=f"https://github.com/DAXXTEAM/SEARCH_BOT"),
],
[
InlineKeyboardButton("𝐂𝐂 𝐁𝐎𝐓", url=f"https://github.com/DAXXTEAM/CC_BOT"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://mallucampaign.in/images/img_1710788470.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
 
   
# --------------


@app.on_message(filters.command("Lundlegakya", prefixes="#"))
@capture_err
async def repo(_, message):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.github.com/repos/DAXXTEAM/DAXXMUSIC/contributors")
    
    if response.status_code == 200:
        users = response.json()
        list_of_users = ""
        count = 1
        for user in users:
            list_of_users += f"{count}. [{user['login']}]({user['html_url']})\n"
            count += 1

        text = f"""[𝖱𝖤𝖯𝖮 𝖫𝖨𝖭𝖪](https://github.com/DAXXTEAM/DAXXMUSIC) | [𝖦𝖱𝖮𝖴𝖯](https://t.me/HEROKUFREECC)
| 𝖢𝖮𝖭𝖳𝖱𝖨𝖡𝖴𝖳𝖮𝖱𝖲 |
----------------
{list_of_users}"""
        await app.send_message(message.chat.id, text=text, disable_web_page_preview=True)
    else:
        await app.send_message(message.chat.id, text="Failed to fetch contributors.")


