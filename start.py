# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

import asyncio
from config import START_PIC
from buttons import start_buttons
from database import add_user

def start_handler(bot, message):

    add_user(message.from_user.id)

    async def run_animation():

        # ================= START ANIMATION =================
        m = await message.reply_text("ᴍᴏɴᴋᴇʏ ᴅ ʟᴜғғʏ\nɢᴇᴀʀ 𝟻...")

        await asyncio.sleep(0.5)
        await m.edit_text("🎊")

        await asyncio.sleep(0.5)
        await m.edit_text("🚀")

        await asyncio.sleep(0.5)
        await m.edit_text("sᴜɴ ɢᴏᴅ ɴɪᴋᴀ!...")

        await asyncio.sleep(0.5)
        await m.delete()

        # ================= STICKER =================
        sticker_msg = await message.reply_sticker(
            "CAACAgQAAxkBAAPZafuA9gQjLstGU0j8kmlDj2-P2A0AAqoaAALVH9BRmAWPD58ZL6keBA"
        )

        # ================= START MESSAGE (MAIN UI) =================
        await sticker_msg.reply_photo(
            photo=START_PIC,
            caption=f"""
ᴡᴇʟᴄᴏᴍᴇ {message.from_user.first_name} ♡, ᴛᴏ ᴀᴅᴠᴀɴᴄᴇᴅ sᴛʀɪᴄᴋᴇʀ ɪᴅ ʙᴏᴛ

 ›› I ᴄᴀɴ ɢᴇɴᴇʀᴀᴛᴇ sᴛʀɪᴄᴋᴇʀ ᴛᴏ ɢɪᴠᴇ ɪᴅ 
 
 ›› Jᴜsᴛ sᴇɴᴅ ᴛʜᴇ Sᴛɪᴄᴋᴇʀ ᴛʜᴇɴ sᴇᴇ ᴍʏ ᴍᴀɢɪᴄ

 ›› ᴘᴏᴡᴇʀᴇᴅ ʙʏ : @Aero_Unity 
""",
            reply_markup=start_buttons()
        )

    # run async animation safely
    bot.loop.create_task(run_animation())

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #
