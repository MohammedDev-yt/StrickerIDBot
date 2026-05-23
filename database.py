
# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

import sqlite3
from config import DB_NAME

conn = sqlite3.connect(DB_NAME, check_same_thread=False)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS stickers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    file_id TEXT,
    unique_id TEXT
)
""")

conn.commit()

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

def add_user(uid):
    cur.execute("INSERT OR IGNORE INTO users VALUES (?)", (uid,))
    conn.commit()

def add_sticker(uid, file_id, unique_id):
    cur.execute(
        "INSERT INTO stickers (user_id, file_id, unique_id) VALUES (?, ?, ?)",
        (uid, file_id, unique_id)
    )
    conn.commit()

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

def get_stats():
    cur.execute("SELECT COUNT(*) FROM users")
    users = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM stickers")
    stickers = cur.fetchone()[0]

    return users, stickers

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

def get_all_users():
    cur.execute("SELECT user_id FROM users")
    return cur.fetchall()

# ===================== ADDED SAFETY FIX (ONLY ADDITION) =====================

import threading

db_lock = threading.Lock()

def safe_execute(query, params=()):
    """Thread-safe DB execution (prevents Render crashes)"""
    with db_lock:
        cur.execute(query, params)
        conn.commit()

# Optional improved wrappers (NOT replacing old code, only extra tools)

def add_user_safe(uid):
    safe_execute("INSERT OR IGNORE INTO users VALUES (?)", (uid,))

def add_sticker_safe(uid, file_id, unique_id):
    safe_execute(
        "INSERT INTO stickers (user_id, file_id, unique_id) VALUES (?, ?, ?)",
        (uid, file_id, unique_id)
    )

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #