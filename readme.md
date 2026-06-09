# Expense Tracker and Budget Analysis System

## Problem Statement

Managing personal expenses manually through notebooks, spreadsheets, or paper records is often inefficient and prone to errors. Individuals frequently face difficulties in tracking spending habits, maintaining monthly budgets, identifying unnecessary expenditures, and generating meaningful financial reports.

The Expense Tracker and Budget Analysis System is a Python-based application developed to simplify personal financial management. The system enables users to record expenses, categorize transactions, track monthly budgets, analyze spending patterns, generate reports, and visualize expenditure trends through charts. SQLite is used for persistent data storage, while Pandas and Matplotlib provide analytical and visualization capabilities.

---

## Features

**Expense Management**

* Add new expenses
* Categorize expenses
* Store expense descriptions
* Maintain transaction history

**Budget Management**

* Monthly budget tracking
* Budget utilization monitoring
* Budget warning alerts
* Remaining budget calculation

**Search and Filtering**

* Search expenses by category
* Search expenses by date range
* View filtered expense records

**Analytics and Reporting**

* Monthly spending summary
* Dashboard statistics
* Top spending category analysis
* Total expense calculation
* Average expense calculation

**Data Visualization**

* Monthly expense trend chart
* Category-wise expense distribution pie chart

**Export Functionality**

* CSV report export

---

## Technologies Used

| Technology | Purpose                       |
| ---------- | ----------------------------- |
| Python     | Application Development       |
| SQLite     | Database Management           |
| Pandas     | Data Analysis                 |
| Matplotlib | Data Visualization            |
| CSV Module | Report Export                 |
| SQL        | Data Querying and Aggregation |

---

## Project Structure

```text
Personal Expense Tracker/
│
├── main.py
├── database.py
├── reports.py
├── visualization.py
├── schema.sql
├── requirements.txt
├── README.md
│
├── data/
│   └── expense_tracker.db
│
├── exports/
│   └── reports.csv
│
├── charts/
│   ├── monthly_expense_chart.png
│   └── category_distribution.png
│
└── screenshots/
    ├── main_menu(1).png
    ├── add_expense(2).png
    ├── monthly_summary(3).png
    ├── budget_status(4).png
    ├── search_category(5).png
    ├── search_date(6).png
    ├── top_category(7).png
    ├── csv_export(8).png
    ├── monthly_trend_chart(9).png
    ├── category_pie_chart(10).png
    ├── dashboard(11).png
    ├── budget_alert(12).png
    └── exit(13).png
```

---

## Database Schema

**Users Table**

| Column  | Type    |
| ------- | ------- |
| user_id | INTEGER |
| name    | TEXT    |

**Categories Table**

| Column        | Type    |
| ------------- | ------- |
| category_id   | INTEGER |
| category_name | TEXT    |

**Expenses Table**

| Column       | Type    |
| ------------ | ------- |
| expense_id   | INTEGER |
| user_id      | INTEGER |
| category_id  | INTEGER |
| amount       | REAL    |
| expense_date | TEXT    |
| description  | TEXT    |

**Budget Table**

| Column        | Type |
| ------------- | ---- |
| month         | TEXT |
| budget_amount | REAL |

---

## SQL Concepts Demonstrated

* SUM()
* AVG()
* COUNT()
* GROUP BY
* ORDER BY
* INNER JOIN
* Aggregate Functions
* Date Filtering
* Database Normalization

---

## How to Run

**Step 1: Clone Repository**

```bash
git clone <repository-url>
```

**Step 2: Move into Project Directory**

```bash
cd ExpenseTrackerProject
```

**Step 3: Install Required Packages**

```bash
pip install -r requirements.txt
```

**Step 4: Run the Application**

```bash
python main.py
```

---

## Screenshots

**Main Menu**

![Main Menu](screenshots/main_menu\(1\).png)

**Adding an Expense**

![Add Expense](screenshots/add_expense\(2\).png)

**Monthly Summary Report**

![Monthly Summary](screenshots/monthly_summary\(3\).png)

**Budget Status**

![Budget Status](screenshots/budget_status\(4\).png)

**Search by Category**

![Search Category](screenshots/search_category\(5\).png)

**Search by Date Range**

![Search Date](screenshots/search_date\(6\).png)

**Top Spending Category**

![Top Category](screenshots/top_category\(7\).png)

**CSV Report Export**

![CSV Export](screenshots/csv_export\(8\).png)

**Monthly Expense Trend Chart**

![Monthly Trend Chart](screenshots/monthly_trend_chart\(9\).png)

**Category Distribution Pie Chart**

![Category Distribution](screenshots/category_pie_chart\(10\).png)

**Dashboard Statistics**

![Dashboard](screenshots/dashboard\(11\).png)

**Budget Alert**

![Budget Alert](screenshots/budget_alert\(12\).png)

**Exit Screen**

![Exit](screenshots/exit\(13\).png)

---

## Future Enhancements

* User Authentication System
* PDF Report Generation
* Email Report Sharing
* Expense Forecasting using Machine Learning
* GUI Version using Tkinter
* Web-Based Dashboard
* Mobile Application Integration

---

## Learning Outcomes

* Database Design using SQLite
* CRUD Operations
* SQL Querying and Aggregation
* Data Analysis using Pandas
* Data Visualization using Matplotlib
* Report Generation
* Budget Tracking and Financial Analysis
* Python Modular Programming

---

## Author

**Tutika Neeraja**

B.Tech Student

Personal Expense Tracker

Academic Year: 2025–2026
