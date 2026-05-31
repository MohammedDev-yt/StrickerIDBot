
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
from pymongo import MongoClient
import os

MONGO_URL = os.environ.get("MONGO_URL")

mongo = MongoClient(MONGO_URL)
db = mongo["StickerBot"]

fsub_col = db["force_sub"]

bot = Client("StickerBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# ================= FORCE SUB (ADD HERE) =================
@bot.on_message(filters.command("fsub"))
def set_fsub(_, msg):

    if msg.from_user.id != OWNER_ID:
        return

    if len(msg.command) < 2:
        return msg.reply_text("Use: /fsub @channel")

    channel = msg.command[1]

    if not channel.startswith("@"):
        channel = "@" + channel

    add_fsub(channel)

    msg.reply_text(f"✅ Added FSub: {channel}")

@bot.on_message(filters.command("nofsub"))
def del_fsub(_, msg):

    if msg.from_user.id != OWNER_ID:
        return

    if len(msg.command) < 2:
        return msg.reply_text("Use: /nofsub @channel")

    channel = msg.command[1]

    if not channel.startswith("@"):
        channel = "@" + channel

    remove_fsub(channel)

    msg.reply_text(f"❌ Removed FSub: {channel}")

@bot.on_message(filters.command("listfsub"))
def list_fsub(_, msg):

    if msg.from_user.id != OWNER_ID:
        return

    channels = get_fsub_channels()

    if not channels:
        return msg.reply_text("No Force Sub channels set.")

    text = "📢 Force Sub Channels:\n\n"
    for ch in channels:
        text += f"• {ch}\n"

    msg.reply_text(text)

from pyrogram.enums import ChatMemberStatus
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_fsubs():
    data = fsub_col.find_one({"_id": "fsubs"})
    if not data:
        return []
    return data.get("channels", [])


def add_fsub(channel):
    fsub_col.update_one(
        {"_id": "fsubs"},
        {"$addToSet": {"channels": channel}},
        upsert=True
    )


def remove_fsub(channel):
    fsub_col.update_one(
        {"_id": "fsubs"},
        {"$pull": {"channels": channel}}
    )

async def check_force_sub(client, user_id):

    # ✅ OWNER BYPASS
    if user_id == OWNER_ID:
        return True

    channels = get_fsubs()

    if not channels:
        return True

    for channel in channels:
        try:
            member = await client.get_chat_member(channel, user_id)

            if member.status not in [
                ChatMemberStatus.MEMBER,
                ChatMemberStatus.ADMINISTRATOR,
                ChatMemberStatus.OWNER
            ]:
                return False

        except:
            return False

    return True


@bot.on_message(filters.private & ~filters.command([
    "start", "stickerid", "stats", "broadcast"
]))
async def force_sub_checker(client, message):

    if not message.from_user:
        return

    channels = get_fsubs()
    if not channels:
        return

    ok = await check_force_sub(client, message.from_user.id)

    if not ok:

        btn = InlineKeyboardMarkup([
            [
                InlineKeyboardButton(
                    "📢 Join Channel",
                    url=f"https://t.me/{FORCE_SUB_CHANNEL.replace('@','')}"
                )
            ]
        ])

        return await message.reply_text(
            "❌ Join our channel to use this bot.",
            reply_markup=btn
        )


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
            continue 

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

    if not msg.from_user:
        return

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