import sqlite3
import os 
from dotenv import load_dotenv 

load_dotenv()


base_dir = os.path.dirname(os.path.abspath(__file__))
db_dir = os.path.join(base_dir ,os.getenv('db_name') )



def create_tables():
    conn = sqlite3.connect(db_dir)
    cur = conn.cursor()

    # questions
    cur.execute('''
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            option1 TEXT NOT NULL,
            option2 TEXT NOT NULL,
            option3 TEXT NOT NULL,
            option4 TEXT NOT NULL,
            correct_option INTEGER NOT NULL
        )
    ''')

    # Results 
    cur.execute('''
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            score INTEGER NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
    print("Tables created successfully!")
