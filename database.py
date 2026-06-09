import sqlite3
import os

DB_PATH = "data/expense_tracker.db"


def connect_db():
    os.makedirs("data", exist_ok=True)
    return sqlite3.connect(DB_PATH)


def initialize_database():

    conn = connect_db()
    cursor = conn.cursor()

    with open("schema.sql", "r") as f:
        cursor.executescript(f.read())

    categories = [
        "Food",
        "Transport",
        "Utilities",
        "Entertainment",
        "Education",
        "Healthcare",
        "Shopping"
    ]

    for cat in categories:
        cursor.execute("""
        INSERT OR IGNORE INTO categories(category_name)
        VALUES(?)
        """, (cat,))

    cursor.execute("""
    INSERT OR IGNORE INTO users(user_id,name)
    VALUES(1,'Student')
    """)

    cursor.execute("""
    INSERT OR IGNORE INTO budget
    (month,budget_amount)
    VALUES('2026-06',10000)
    """)

    conn.commit()
    conn.close()