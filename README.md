# 📚 Books to Scrape — End-to-End (Scrape → Clean → Analyze → Dashboard)

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-dashboard-red)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-brightgreen)

An educational project that scrapes [Books to Scrape](http://books.toscrape.com/), cleans the data, stores it (CSV + SQLite), analyzes it, and visualizes insights in a Streamlit dashboard.  

---

##  Features
-  **Scraping**: BeautifulSoup scraper with polite delays & retries  
-  **Data storage**: CSV (`data/books.csv`) + SQLite (`data/books.db`)  
-  **Analysis**: Data cleaning and simple EDA  
- **Dashboard**: Interactive Streamlit app for filtering, searching, and visualizing  

---

##  Installation

```bash
# Clone the repository
git clone https://github.com/22Ifeoma22/books-scrape-dashboard.git
cd books-scrape-dashboard

# Create virtual environment (optional but recommended)
python -m venv .venv
.\.venv\Scripts\activate    # on Windows
source .venv/bin/activate   # on Mac/Linux

# Install dependencies
pip install -r requirements.txt

## 📸 Visuals

![Price Distribution](screenshots/price_hist.png)
![Ratings Distribution](screenshots/rating_hist.png)
![Top Categories](screenshots/top_categories.png)
![Average Price by Category](screenshots/avg_price_by_category.png)
