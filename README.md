# Web Scraper for Amazon
# 📊 Amazon Laptop Prices and Ratings Dashboard

This project is a **Streamlit** web application that provides interactive visualizations and insights into the prices and ratings of laptops listed on Amazon. The dashboard allows users to filter laptops based on price and rating, view different types of data visualizations, and perform sentiment analysis on placeholder reviews.

## 🚀 Features

- **Price Range Filtering**: Filter laptops by selecting a price range.
- **Rating Range Filtering**: Filter laptops by selecting a rating range.
- **Top Value for Money Laptops**: See the top 10 laptops with the best value (highest rating per price).
- **Visualizations**:
  - **Price Distribution**: A histogram that shows the distribution of laptop prices.
  - **Word Cloud**: A word cloud generated from the product names of the laptops.
  - **Correlation Heatmap**: A heatmap showing the correlation between price and rating.
  - **Sentiment Analysis**: Sentiment scores of placeholder reviews using VADER sentiment analysis.
- **Download Filtered Data**: Download the filtered dataset as a CSV file.
- **Summary Metrics**: Average price and rating of the filtered laptops.

## 🛠️ Installation

### Prerequisites
- Python 3.7 or later
- **pip** for managing Python packages

### Install Dependencies

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/your-repository-name.git

2. Navigate to the project directory:
     ```bash
   cd your-repository-name

3. Install the required packages
      ```bash
   pip install -r requirements.txt


### Run Streamlit App
 ```bash
streamlit run testdb.py
 ```
Once the server starts, open your browser and go to http://localhost:8501 to access the dashboard.

### File Structure
📦data-scraping/
 ┣ 📂data/
 ┃ ┗ 📜amazon_products.csv
 ┣ 📜scrape.py
 ┣ 📜testdb.py
 ┣ 📜requirements.txt
 ┣ 📜README.md
 ┣ 📜.gitignore
 


