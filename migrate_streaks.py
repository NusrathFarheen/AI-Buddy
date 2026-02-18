import sqlite3
import os

DB_PATH = "planner.db" # Running from root usually, but let's be safe

def add_columns():
    if not os.path.exists(DB_PATH):
        # Try finding it in backend if running from root
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
        cursor.execute("ALTER TABLE routines ADD COLUMN current_streak INTEGER DEFAULT 0")
        print("current_streak added.")
    except Exception as e:
        print(f"Error adding current_streak: {e}")

    try:
        cursor.execute("ALTER TABLE routines ADD COLUMN best_streak INTEGER DEFAULT 0")
        print("best_streak added.")
    except Exception as e:
        print(f"Error adding best_streak: {e}")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    add_columns()
