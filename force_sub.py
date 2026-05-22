# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database import get_channels


def join_buttons():
    buttons = []

    channels = get_channels()

    for ch in channels:
        buttons.append([
            InlineKeyboardButton(
                f"›› ‼️ ʟᴏᴏᴋs ʟɪᴋᴇ ʏᴏᴜ ʜᴀᴠᴇɴ'ᴛ ᴊᴏɪɴᴇᴅ ᴛᴏ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ʏᴇᴛ, sᴜʙsᴄʀɪʙᴇ ɴᴏw... {ch}",
                url=f"https://t.me/{ch.replace('@','')}"
            )
        ])

    buttons.append([
        InlineKeyboardButton("🔄 Tʀʏ Aɢᴀɪɴ", callback_data="check_join")
    ])

    return InlineKeyboardMarkup(buttons)

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

async def check_user(bot, user_id):

    channels = get_channels()

    for ch in channels:
        try:
            member = await bot.get_chat_member(ch, user_id)
            if member.status not in ["member", "administrator", "creator"]:
                return False
        except:
            return False

    return True

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #
