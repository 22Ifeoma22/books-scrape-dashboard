# Books to Scrape — End-to-End (Scrape → Clean → Analyze → Dashboard)

Educational project that scrapes [books.toscrape.com], cleans the data, stores it (CSV + SQLite), analyzes it, and visualizes insights in a Streamlit dashboard.

## Features
- Requests + BeautifulSoup scraper with polite delays and retries
- CSV output (`data/books.csv`) and **SQLite** database (`data/books.db`)
- Pandas analysis (category counts, avg prices, rating distribution)
- Streamlit dashboard with filters + export

## Quickstart

```bash
# 1) Create & activate venv (Windows PowerShell)
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1

# 2) Install deps
python -m pip install --upgrade pip
pip install -r requirements.txt

# 3) Scrape (writes data/books.csv)
python scraper/scrape_books_to_scrape.py

# 4) (Optional) Save to SQLite
python scraper/save_to_sqlite.py

# 5) Run dashboard
python -m streamlit run app/streamlit_books_dashboard.py
## Usage

### 1. Clone and setup
```bash
git clone https://github.com/22Ifeoma22/books-scrape-dashboard.git
cd books-scrape-dashboard
python -m venv .venv
.venv\Scripts\activate   # Windows
##  How to Run the Project

### Step 1: Run the scraper (to refresh books.csv)
```powershell
python .\scrape_books_to_scrape.py
