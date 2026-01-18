import requests
from bs4 import BeautifulSoup
import pandas as pd

def price_comparing():
    url = "http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html"
    headers = {"User-Agent": "Mozilla/5.0"}

    try: 
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        books = []
        articles = soup.find_all('article', class_='product_pod')

        for art in articles:
            title = art.h3.a['title']

            price_text = art.find('p', class_='price_color').get_text()
            price = float(''.join(c for c in price_text if c.isdigit() or c == '.'))

            stock = art.find('p', class_='instock availability').get_text(strip=True)

            rating_classes = art.find('p', class_='star-rating')['class']
            rating = rating_classes[1] 

            books.append({
                "Title": title,
                "Price (£)": price,
                "Stock": stock,
                "Rating": rating
            })

        df = pd.DataFrame(books)
        avg_price = df["Price (£)"].mean()
            
        print(f"✅ {len(books)} articles trouvés.")
        print(f"📊 Prix moyen de la sélection : {avg_price:.2f}£")
        
        # Export
        df.to_csv("ecommerce_report.csv", index=False)
        print("💾 Rapport généré : ecommerce_report.csv")

    except Exception as e:
        print(f"Error happened: {e}")


if __name__ == "__main__":
    price_comparing()