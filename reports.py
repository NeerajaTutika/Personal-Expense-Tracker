import sqlite3

DB_PATH = "data/expense_tracker.db"


def monthly_summary():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    query = """
    SELECT strftime('%Y-%m', expense_date),
           SUM(amount)
    FROM expenses
    GROUP BY strftime('%Y-%m', expense_date)
    ORDER BY 1;
    """

    cursor.execute(query)

    rows = cursor.fetchall()

    print("\nMONTHLY SUMMARY")
    print("-" * 30)

    for row in rows:
        print(f"{row[0]} : ₹{row[1]:.2f}")

    conn.close()


def top_category():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    query = """
    SELECT c.category_name,
           SUM(e.amount)
    FROM expenses e
    JOIN categories c
    ON e.category_id = c.category_id
    GROUP BY c.category_name
    ORDER BY SUM(e.amount) DESC
    LIMIT 1
    """

    cursor.execute(query)

    result = cursor.fetchone()

    if result:
        print("\nTop Spending Category")
        print(result[0], "₹", result[1])

    conn.close()

def dashboard_stats():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT SUM(amount),AVG(amount),COUNT(*)
    FROM expenses
    """)

    result = cursor.fetchone()

    total = result[0] or 0
    avg_expense = result[1] or 0
    count = result[2] or 0

    cursor.execute("""
    SELECT c.category_name,SUM(e.amount)
    FROM expenses e
    JOIN categories c
    ON e.category_id=c.category_id
    GROUP BY c.category_name
    ORDER BY SUM(e.amount) DESC
    LIMIT 1
    """)

    top = cursor.fetchone()

    print("\n========== DASHBOARD ==========")
    print(f"Total Expenses     : ₹{total:.2f}")
    print(f"Average Expense    : ₹{avg_expense:.2f}")
    print(f"Transactions       : {count}")

    if top:
        print(f"Top Category       : {top[0]}")

    print("=" * 30)

    conn.close()