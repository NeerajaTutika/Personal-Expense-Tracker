CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_name TEXT UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS expenses (
    expense_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    category_id INTEGER,
    amount REAL NOT NULL,
    expense_date TEXT NOT NULL,
    description TEXT,

    FOREIGN KEY(user_id)
        REFERENCES users(user_id),

    FOREIGN KEY(category_id)
        REFERENCES categories(category_id)
);

CREATE TABLE IF NOT EXISTS budget(
    month TEXT PRIMARY KEY,
    budget_amount REAL NOT NULL
);