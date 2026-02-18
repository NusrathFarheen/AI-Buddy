import sqlite3
import os

DB_PATH = "planner.db"

def add_creations_table():
    if not os.path.exists(DB_PATH):
        if os.path.exists("backend/planner.db"):
            db_path = "backend/planner.db"
        else:
            print("DB not found")
            return
    else:
        db_path = DB_PATH
        
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS creations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            type TEXT DEFAULT 'note',
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        print("Table 'creations' created successfully.")
    except Exception as e:
        print(f"Error creating table: {e}")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    add_creations_table()
