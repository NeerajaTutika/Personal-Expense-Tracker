import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os

DB_PATH = "data/expense_tracker.db"


def monthly_chart():

    conn = sqlite3.connect(DB_PATH)

    query = """
    SELECT strftime('%Y-%m', expense_date) AS month,
           SUM(amount) AS total
    FROM expenses
    GROUP BY month
    ORDER BY month
    """

    df = pd.read_sql_query(query, conn)

    if len(df) == 0:
        print("No data found")
        return

    plt.figure(figsize=(8,5))
    plt.plot(df["month"], df["total"], marker="o")

    plt.title("Monthly Expenses")
    plt.xlabel("Month")
    plt.ylabel("Amount")

    plt.grid(True)

    plt.savefig("charts/monthly_expense_chart.png")

    plt.show()

    conn.close()

def category_pie_chart():

    os.makedirs("charts", exist_ok=True)

    conn = sqlite3.connect(DB_PATH)

    query = """
    SELECT c.category_name,
           SUM(e.amount)
    FROM expenses e
    JOIN categories c
    ON e.category_id=c.category_id
    GROUP BY c.category_name
    """

    df = pd.read_sql_query(query, conn)

    if len(df) == 0:
        print("No data available")
        return

    plt.figure(figsize=(8,8))

    plt.pie(
        df.iloc[:,1],
        labels=df.iloc[:,0],
        autopct="%1.1f%%"
    )

    plt.title("Expense Distribution by Category")

    plt.savefig(
        "charts/category_distribution.png"
    )

    plt.show()

    conn.close()