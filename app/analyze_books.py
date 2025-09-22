import pandas as pd, re
df = pd.read_csv("data/books.csv")
df["price_clean"] = df["price"].apply(lambda p: float(re.sub(r"[^\d.]", "", str(p))))
rating_map = {"One":1,"Two":2,"Three":3,"Four":4,"Five":5}
df["rating_num"] = df["rating"].map(rating_map)

print("Top 5 categories:\n", df["category"].value_counts().head(), "\n")
print("Avg price per category (top 5):\n",
      df.groupby("category")["price_clean"].mean().sort_values(ascending=False).head(), "\n")
print("Ratings distribution:\n", df["rating_num"].value_counts().sort_index(), "\n")
print("Most expensive:\n", df.loc[df["price_clean"].idxmax(), ["title","category","price_clean"]], "\n")
