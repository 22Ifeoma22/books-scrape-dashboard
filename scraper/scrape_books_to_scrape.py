# scraper/scrape_books_to_scrape.py
import time, csv
from pathlib import Path
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

BASE_URL = "http://books.toscrape.com/"
CATALOGUE_URL = urljoin(BASE_URL, "catalogue/")
DATA_DIR = Path("data"); DATA_DIR.mkdir(parents=True, exist_ok=True)
OUT_CSV = DATA_DIR / "books.csv"

def get_soup(url: str) -> BeautifulSoup:
    """Fetch a URL and return a BeautifulSoup parser"""
    resp = requests.get(url)
    resp.raise_for_status()
    return BeautifulSoup(resp.text, "html.parser")

def scrape_books():
    books = []
    page = 1
    while True:
        url = urljoin(CATALOGUE_URL, f"page-{page}.html")
        print(f"Scraping page {page}: {url}")
        resp = requests.get(url)
        if resp.status_code == 404:
            break
        soup = BeautifulSoup(resp.text, "html.parser")
        for article in soup.select("article.product_pod"):
            title = article.h3.a["title"]
            price = article.select_one(".price_color").text.strip()
            rating = article.p["class"][-1]
            rel_link = article.h3.a["href"]
            product_url = urljoin(CATALOGUE_URL, rel_link)
            books.append({
                "title": title,
                "price": price,
                "rating": rating,
                "product_url": product_url,
                "category": None  # left blank for now
            })
        page += 1
        time.sleep(0.5)
    return books

def save_csv(books):
    with OUT_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=books[0].keys())
        writer.writeheader()
        writer.writerows(books)
    print(f"Done. Collected {len(books)} books -> {OUT_CSV}")

if __name__ == "__main__":
    books = scrape_books()
    if books:
        save_csv(books)
