import sqlite3
import os

# DB is in current directory
DB_PATH = "planner.db"

def add_column():
    if not os.path.exists(DB_PATH):
        print(f"Error: {DB_PATH} not found.")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    try:
        cursor.execute("ALTER TABLE routines ADD COLUMN last_completed_date TEXT")
        print("Column added successfully.")
    except Exception as e:
        print(f"Error (column might exist): {e}")
    conn.commit()
    conn.close()

if __name__ == "__main__":
    add_column()
