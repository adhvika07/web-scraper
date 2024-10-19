from bs4 import BeautifulSoup
import requests
import pandas as pd

# URL of the product page
url = 'https://www.amazon.com/s?k=laptop'

# Send request to fetch HTML content
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'DNT': '1',  # Do Not Track Request Header
    'Connection': 'keep-alive'
}

response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Example: Extract product names, prices, and ratings
    products = []
    for item in soup.find_all('div', {'data-component-type': 's-search-result'}):
        name = item.h2.text.strip()

        # Extract price
        price = None
        price_span = item.find('span', 'a-offscreen')
        if price_span:
            price = price_span.text.strip()
        
        # Extract rating
        rating = None
        rating_span = item.find('span', 'a-icon-alt')
        if rating_span:
            rating = rating_span.text.strip()

        # Append to product list
        products.append([name, price, rating])

    # Convert to DataFrame
    df = pd.DataFrame(products, columns=['Product Name', 'Price', 'Rating'])

    # Save the data to CSV
    df.to_csv('amazon_products.csv', index=False)
    print(df.head())

    # Clean 'Price' by removing dollar sign and commas
    df['Price'] = df['Price'].replace({'\$': '', ',': ''}, regex=True)

    # Convert 'Price' to numeric, ignoring errors and coercing invalid entries to NaN
    df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

    # Clean 'Rating' and extract numeric values
    df['Rating'] = df['Rating'].str.extract('(\d+\.\d+)').astype(float)

    # Calculate average price and rating
    avg_price = df['Price'].mean()
    avg_rating = df['Rating'].mean()

    print(f"Average Price: ${avg_price:.2f}")
    print(f"Average Rating: {avg_rating:.2f}")

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
