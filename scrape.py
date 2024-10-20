from bs4 import BeautifulSoup
import requests
import pandas as pd


url = 'https://www.amazon.com/s?k=laptop'


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'DNT': '1',  
    'Connection': 'keep-alive'
}

response = requests.get(url, headers=headers)


if response.status_code == 200:
   
    soup = BeautifulSoup(response.content, 'html.parser')

    
    products = []
    for item in soup.find_all('div', {'data-component-type': 's-search-result'}):
        name = item.h2.text.strip()

        
        price = None
        price_span = item.find('span', 'a-offscreen')
        if price_span:
            price = price_span.text.strip()
        
        
        rating = None
        rating_span = item.find('span', 'a-icon-alt')
        if rating_span:
            rating = rating_span.text.strip()

        
        products.append([name, price, rating])

    
    df = pd.DataFrame(products, columns=['Product Name', 'Price', 'Rating'])

   
    df.to_csv('amazon_products.csv', index=False)
    print(df.head())

    
    df['Price'] = df['Price'].replace({'\$': '', ',': ''}, regex=True)

    
    df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

    
    df['Rating'] = df['Rating'].str.extract('(\d+\.\d+)').astype(float)

  
    avg_price = df['Price'].mean()
    avg_rating = df['Rating'].mean()

    print(f"Average Price: ${avg_price:.2f}")
    print(f"Average Rating: {avg_rating:.2f}")

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
