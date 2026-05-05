# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

def start_buttons():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("• ʜᴇʟᴘ •", callback_data="help"),
            InlineKeyboardButton("• ᴀʙᴏᴜᴛ •", callback_data="about")
        ],
        [
            InlineKeyboardButton("• ᴏᴡɴᴇʀ •", callback_data="owner"),
            InlineKeyboardButton("• ᴜᴘᴅᴀᴛᴇs •", callback_data="updates")
        ],
        [
            InlineKeyboardButton("• sᴛᴀᴛs •", callback_data="stats_cmd")
        ]
    ])

def home():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("• ʜᴏᴍᴇ •", callback_data="home")]
    ])

def copy_buttons(file_id):
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("• ᴄᴏᴘʏ ғɪʟᴇ ɪᴅ •", callback_data=f"copy|{file_id}")],
        [InlineKeyboardButton("• ʜᴏᴍᴇ •", callback_data="home")]
    ])

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #
