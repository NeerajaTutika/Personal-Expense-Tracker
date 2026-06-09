import sqlite3
import csv
import os

from database import initialize_database

from reports import (
    monthly_summary,
    top_category,
    dashboard_stats
)

from visualization import (
    monthly_chart,
    category_pie_chart
)

DB_PATH = "data/expense_tracker.db"

BUDGET = 10000


def add_expense():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    print("\n========== CATEGORIES ==========")
    print("1. Food")
    print("2. Transport")
    print("3. Utilities")
    print("4. Entertainment")
    print("5. Education")
    print("6. Healthcare")
    print("7. Shopping")

    category = int(input("\nCategory ID: "))
    amount = float(input("Amount (₹): "))
    date = input("Date (YYYY-MM-DD): ")
    description = input("Description: ")

    cursor.execute("""
    INSERT INTO expenses
    (user_id, category_id, amount,
     expense_date, description)

    VALUES(1,?,?,?,?)
    """, (category, amount, date, description))

    conn.commit()
    conn.close()

    print("\n✅ Expense Added Successfully")


def budget_status():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT SUM(amount)
    FROM expenses
    """)

    total = cursor.fetchone()[0]

    if total is None:
        total = 0

    print("\n========== BUDGET STATUS ==========")
    print(f"Budget Amount : ₹{BUDGET}")
    print(f"Spent         : ₹{total}")
    print(f"Remaining     : ₹{BUDGET - total}")

    conn.close()


def budget_alert():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT budget_amount
    FROM budget
    WHERE month='2026-06'
    """)

    result = cursor.fetchone()

    if result is None:
        print("Budget not configured")
        return

    budget = result[0]

    cursor.execute("""
    SELECT SUM(amount)
    FROM expenses
    """)

    spent = cursor.fetchone()[0] or 0

    usage = (spent / budget) * 100

    print("\n========== BUDGET ALERT ==========")
    print(f"Budget Amount : ₹{budget}")
    print(f"Spent         : ₹{spent}")
    print(f"Usage         : {usage:.2f}%")

    if usage >= 100:
        print("⚠ Budget Exceeded")

    elif usage >= 80:
        print("⚠ Warning: Budget reached 80%")

    else:
        print("✅ Budget usage is healthy")

    conn.close()


def search_by_category():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    print("""
Available Categories

Food
Transport
Utilities
Entertainment
Education
Healthcare
Shopping
""")

    category = input("Enter Category Name: ")

    query = """
    SELECT expense_date,
           amount,
           description
    FROM expenses e
    JOIN categories c
    ON e.category_id=c.category_id
    WHERE c.category_name=?
    """

    cursor.execute(query, (category,))
    rows = cursor.fetchall()

    print("\n========== SEARCH RESULTS ==========")

    if len(rows) == 0:
        print("No records found")

    for row in rows:
        print(row)

    conn.close()


def search_by_date():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    start = input("Start Date (YYYY-MM-DD): ")
    end = input("End Date (YYYY-MM-DD): ")

    cursor.execute("""
    SELECT *
    FROM expenses
    WHERE expense_date
    BETWEEN ? AND ?
    """, (start, end))

    rows = cursor.fetchall()

    print("\n========== DATE SEARCH RESULTS ==========")

    if len(rows) == 0:
        print("No records found")

    for row in rows:
        print(row)

    conn.close()


def export_report():

    os.makedirs("exports", exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM expenses
    """)

    rows = cursor.fetchall()

    with open(
            "exports/reports.csv",
            "w",
            newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "ExpenseID",
            "UserID",
            "CategoryID",
            "Amount",
            "Date",
            "Description"
        ])

        writer.writerows(rows)

    conn.close()

    print("\n✅ Report Exported Successfully")
    print("Saved as: exports/reports.csv")


def menu():

    while True:

        print("""
================================================
      EXPENSE TRACKER & BUDGET ANALYSIS
================================================

1. Add Expense
2. Monthly Summary
3. Budget Status
4. Search By Category
5. Search By Date Range
6. Top Spending Category
7. Export CSV Report
8. Monthly Trend Chart
9. Category Pie Chart
10. Dashboard Statistics
11. Budget Alert
12. Exit

================================================
""")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            monthly_summary()

        elif choice == "3":
            budget_status()

        elif choice == "4":
            search_by_category()

        elif choice == "5":
            search_by_date()

        elif choice == "6":
            top_category()

        elif choice == "7":
            export_report()

        elif choice == "8":
            monthly_chart()

        elif choice == "9":
            category_pie_chart()

        elif choice == "10":
            dashboard_stats()

        elif choice == "11":
            budget_alert()

        elif choice == "12":
            print("\nThank you for using Expense Tracker.")
            break

        else:
            print("\n❌ Invalid Choice")


if __name__ == "__main__":
    initialize_database()
    menu()