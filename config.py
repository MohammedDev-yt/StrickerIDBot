# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

import os

# ================= SAFE ENV HANDLING =================
API_ID = int(os.environ.get("API_ID", "0"))
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

OWNER_ID = int(os.environ.get("OWNER_ID", "0"))
OWNER_NAME = os.environ.get("OWNER_NAME", "Mᴏʜᴀᴍᴍᴇᴅ")

START_PIC = os.environ.get(
    "START_PIC",
    "https://graph.org/file/cb707ebcf6e087d4a49c6-ce0dbf8bc97b6dd50b.jpg"
)

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

# ================= VALIDATION (ADDED ONLY - DO NOT REMOVE EXISTING CODE) =================

if API_ID == 0:
    print("❌ ERROR: API_ID not set in environment variables")

if not API_HASH:
    print("❌ ERROR: API_HASH not set in environment variables")

if not BOT_TOKEN:
    print("❌ ERROR: BOT_TOKEN not set in environment variables")

if OWNER_ID == 0:
    print("⚠️ WARNING: OWNER_ID is 0. Set it in Render ENV or bot will break permissions")


# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

DB_NAME = "bot.db"

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #