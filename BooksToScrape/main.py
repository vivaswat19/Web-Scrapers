from bs4 import BeautifulSoup
import urllib.request
import pandas as pd


dataset = []
for page_count in range(1, 51):
    url = f"http://books.toscrape.com/catalogue/page-{page_count}.html"
    print(url)
    html_resp = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html_resp, 'html.parser')
    books = soup.select('ol.row li')

    for book in books:
        image_link = book.select('.image_container a img')[0].attrs['src']
        book_name = book.select('h3 a')[0].attrs['title']
        book_price = book.select('.product_price  .price_color')[0].get_text()
        dataset.append([image_link, book_name, book_price])

ds = pd.DataFrame(data=dataset, columns=['image_url', 'book_title', 'product_price'])

ds.to_csv('/Users/vivaswatsinha/Desktop/Github/Web-Scrapers/BooksToScrape/final.csv', index=False)