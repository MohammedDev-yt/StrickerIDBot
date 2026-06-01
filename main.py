
# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

from pyrogram import Client, filters
import time

from config import API_ID, API_HASH, BOT_TOKEN, OWNER_ID
from keep_alive import keep_alive

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

from start import start_handler
from sticker import ask_sticker, handle_sticker
from callback import callback_handler
from database import add_user, get_stats, get_all_users
from utils import START_TIME, VERSION 

bot = Client("StickerBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

broadcast_mode = set()

# ================= START =================
@bot.on_message(filters.command("start"))
def start(_, msg):
    start_handler(bot, msg)

# ================= STICKER =================
@bot.on_message(filters.command("stickerid"))
def ask(_, msg):
    ask_sticker(bot, msg)

@bot.on_message(filters.sticker)
def sticker(_, msg):
    handle_sticker(bot, msg)

# ================= STATS (OWNER ONLY) =================
@bot.on_message(filters.command("stats"))
def stats(_, msg):
    if msg.from_user.id != OWNER_ID:
        msg.reply_text("Yᴏᴜ Aʀᴇ Nᴏᴛ Mʏ Mᴀsᴛᴇʀ.")
        return

    start_ping = time.time()
    users, stickers = get_stats()
    ping = round((time.time() - start_ping) * 1000, 2)

    uptime_sec = int(time.time() - START_TIME)

    # format uptime
    days = uptime_sec // 86400
    hours = (uptime_sec % 86400) // 3600
    minutes = (uptime_sec % 3600) // 60
    seconds = uptime_sec % 60

    uptime = f"{days}d {hours}h {minutes}m {seconds}s"

    msg.reply_text(f"""
📊 𝗕𝗼𝘁 𝗦𝘁𝗮𝘁𝘀

👥 Tᴏᴛᴀʟ Usᴇʀs: {users}
🎯  Tᴏᴛᴀʟ Sᴛɪᴄᴋᴇʀs: {stickers}
⚡ Pɪɴɢ: {ping} ms
⏱ Uᴘᴛɪᴍᴇ: {uptime}
🧬 Vᴇʀsɪᴏɴ: {VERSION}
""")

# ================= BROADCAST (OWNER ONLY) =================
@bot.on_message(filters.command("broadcast"))
def broadcast(_, msg):
    if msg.from_user.id != OWNER_ID:
        msg.reply_text("Yᴏᴜ Aʀᴇ Nᴏᴛ Mʏ Mᴀsᴛᴇʀ")
        return

    broadcast_mode.add(msg.from_user.id)
    msg.reply_text("📢 Sᴇɴᴅ Mᴇssᴀɢᴇ Tᴏ Bʀᴏᴀᴅᴄᴀsᴛ")

# ================= BROADCAST MESSAGE HANDLER =================
@bot.on_message(filters.private & filters.text)
def send_broadcast(_, msg):

    if msg.from_user.id not in broadcast_mode:
        return

    users = get_all_users()

    ok = 0
    fail = 0

    for u in users:
        try:
            bot.send_message(u[0], msg.text)
            ok += 1
        except:
            fail += 1

    msg.reply_text(
        f"📢 𝗗𝗼𝗻𝗲\n✔ Sent: {ok}\n❌ Failed: {fail}"
    )

    broadcast_mode.remove(msg.from_user.id)

# ================= CALLBACK =================
@bot.on_callback_query()
def cb(_, q):
    callback_handler(bot, q)

# ================= SAVE USER (ADD HERE) =================
@bot.on_message(filters.private)
def save_user(_, msg):
    try:
        add_user(msg.from_user.id)
    except:
        pass

# ================= START BOT =================
if __name__ == "__main__":
    keep_alive()
    print("Bot Running...")
    bot.run()

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #