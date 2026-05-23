# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

import time
from buttons import start_buttons, home
from database import get_stats
from config import OWNER_NAME, OWNER_ID, START_PIC
from utils import START_TIME, VERSION

def callback_handler(bot, q):

    data = q.data

    if data == "home":
        try:
            q.message.edit_caption(
                caption=f"""
ᴡᴇʟᴄᴏᴍᴇ ʙᴀᴄᴋ {q.from_user.first_name} ♡, ᴛᴏ ᴀᴅᴠᴀɴᴄᴇᴅ sᴛʀɪᴄᴋᴇʀ ɪᴅ ʙᴏᴛ

›› I ᴄᴀɴ ɢᴇɴᴇʀᴀᴛᴇ sᴛʀɪᴄᴋᴇʀ ᴛᴏ ɢɪᴠᴇ ɪᴅ 
 
›› Jᴜsᴛ sᴇɴᴅ ᴛʜᴇ Sᴛɪᴄᴋᴇʀ ᴛʜᴇɴ sᴇᴇ ᴍʏ ᴍᴀɢɪᴄ

›› ᴘᴏᴡᴇʀᴇᴅ ʙʏ : @Anime_UpdatesAU 
""",
                reply_markup=start_buttons()
            )
        except:
            q.message.reply_photo(
                photo=START_PIC,
                caption=f"""
ᴡᴇʟᴄᴏᴍᴇ ʙᴀᴄᴋ {q.from_user.first_name} ♡, ᴛᴏ ᴀᴅᴠᴀɴᴄᴇᴅ sᴛʀɪᴄᴋᴇʀ ɪᴅ ʙᴏᴛ

›› I ᴄᴀɴ ɢᴇɴᴇʀᴀᴛᴇ sᴛʀɪᴄᴋᴇʀ ᴛᴏ ɢɪᴠᴇ ɪᴅ 
 
›› Jᴜsᴛ sᴇɴᴅ ᴛʜᴇ Sᴛ𝗶𝗰𝗸𝗲𝗿 ᴛʜᴇɴ sᴇᴇ ᴍʏ ᴍᴀɢɪᴄ

›› ᴘᴏᴡᴇʀᴇᴅ ʙʏ : @Anime_UpdatesAU 
""",
                reply_markup=start_buttons()
            )

    elif data == "help":
        try:
            q.message.edit_caption(
                caption="𝗵𝗼𝘄 𝘁𝗼 𝘀𝗲𝗻𝗱 𝘀𝘁𝗶𝗰𝗸𝗲𝗿\n\nUse /stickerid command then send sticker",
                reply_markup=home()
            )
        except:
            q.message.edit_text(
                "𝗵𝗼𝘄 𝘁𝗼 𝘀𝗲𝗻𝗱 𝘀𝘁𝗶𝗰𝗸𝗲𝗿\n\nUse /stickerid command then send sticker",
                reply_markup=home()
            )

    elif data == "about":
        text = """
ℹ️ <b>Sticker ID Bot</b>

🤖 Nᴀᴍᴇ : <a href="http://t.me/AU_StickerID_bot">AU Sticker ID Bot</a>
📚 Lɪʙʀᴀʀʏ: Pʏʀᴏɢʀᴀᴍ
💻 Lᴀɴɢᴜᴀɢᴇ: Pʏᴛʜᴏɴ 𝟹
⚙️ Sᴇʀᴠᴇʀ: <a href="https://render.com/">Rᴇɴᴅᴇʀ</a> 
🚀 Bᴜɪʟᴅ Sᴛᴀᴛᴜs: <a href="https://t.me/BotsServerDead">Sᴛᴀʙʟᴇ ✅</a>
👨‍💻 Pʀᴏɢʀᴀᴍᴍᴇʀ: <a href="https://t.me/Mr_Mohammed_29">Mᴏʜᴀᴍᴍᴇᴅ</a>
📢 Uᴘᴅᴀᴛᴇs: <a href="https://t.me/Anime_UpdatesAU">Cʟɪᴄᴋ Hᴇʀᴇ</a>
🌐 Sᴏᴜʀᴄᴇ Cᴏᴅᴇ: <a href="https://github.com/MD-Developer-yt/StrickerIDBot">Gɪᴛʜᴜʙ</a>
"""
        try:
            q.message.edit_caption(
                caption=text,
                reply_markup=home(),
                disable_web_page_preview=True
            )
        except:
            q.message.edit_text(
                text,
                reply_markup=home(),
                disable_web_page_preview=True
            )

    elif data == "owner":
        try:
            q.message.edit_caption(
                caption=f"👑 Owner: {OWNER_NAME}",
                reply_markup=home()
            )
        except:
            q.message.edit_text(
                f"👑 Owner: {OWNER_NAME}",
                reply_markup=home()
            )

    elif data == "updates":
        try:
            q.message.edit_caption(
                caption="›› Stay updated on @Anime_UpdatesAU",
                reply_markup=home()
            )
        except:
            q.message.edit_text(
                "›› Stay updated on @Anime_UpdatesAU",
                reply_markup=home()
            )

    elif data == "stats_cmd":
        if q.from_user.id != OWNER_ID:
            q.answer("Yᴏᴜ Aʀᴇ Nᴏᴛ Mʏ Mᴀsᴛᴇʀ", show_alert=True)
            return

        start_ping = time.time()
        users, stickers = get_stats()
        ping = round((time.time() - start_ping) * 1000, 2)

        uptime_sec = int(time.time() - START_TIME)

        days = uptime_sec // 86400
        hours = (uptime_sec % 86400) // 3600
        minutes = (uptime_sec % 3600) // 60
        seconds = uptime_sec % 60

        uptime = f"{days}d {hours}h {minutes}m {seconds}s"

        text = f"""
📊 𝗕𝗼𝘁 𝗦𝘁𝗮𝘁𝘀

👥 Tᴏᴛᴀʟ Usᴇʀs: {users}
🎯 Tᴏᴛᴀʟ Sᴛɪᴄᴋᴇʀs: {stickers}
⚡ Pɪɴɢ: {ping} ms
⏱ Uᴘᴛɪᴍᴇ: {uptime}
🧬 Vᴇʀsɪᴏɴ: {VERSION}
"""
        try:
            q.message.edit_caption(text, reply_markup=home())
        except:
            q.message.edit_text(text, reply_markup=home())

    elif data.startswith("copy"):
        q.answer("Cᴏᴘɪᴇᴅ ✔", show_alert=True)


# ===================== SAFETY FIX =====================
    try:
        if data is None:
            return
    except:
        pass


# ===================== ERROR HANDLER =====================
def safe_edit(msg, text, reply_markup=None):
    try:
        msg.edit_text(text, reply_markup=reply_markup)
    except:
        pass

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #