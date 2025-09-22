# scraper/save_to_sqlite.py
import sqlite3
import pandas as pd
from pathlib import Path

DATA_DIR = Path("data")
CSV_PATH = DATA_DIR / "books.csv"
DB_PATH = DATA_DIR / "books.db"

def save_to_sqlite(csv_path=CSV_PATH, db_path=DB_PATH):
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV not found: {csv_path}")

    df = pd.read_csv(csv_path)

    # Open SQLite connection
    conn = sqlite3.connect(db_path)
    df.to_sql("books", conn, if_exists="replace", index=False)
    conn.close()

    print(f"Saved {len(df)} books into {db_path}")

if __name__ == "__main__":
    save_to_sqlite()
