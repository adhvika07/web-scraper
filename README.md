# Web Scraper for Amazon
# 📊 Amazon Laptop Prices and Ratings Dashboard

This project is a **Streamlit** web application that provides interactive visualizations and insights into the prices and ratings of laptops listed on Amazon. The dashboard allows users to filter laptops based on price and rating, view different types of data visualizations, and perform sentiment analysis on reviews, if they exist.

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

### 📂 File Structure

- **amazon_products.csv**: File containing the data scraped from Amazon 
- **scraoe.py**: Main Python script for scraping data and generating .csv file
- **testdb.py**: Main Python script for running the Streamlit dashboard.
- **requirements.txt**: Lists all the dependencies required for the project.
- **README.md**: This file contains the project description and instructions.


### 📊 Data
The dataset created by the scrape.py file contains the following headers:

- **Product Name**: The name of the laptop.
- **Price**: The price of the laptop in USD.
- **Rating**: The average customer rating of the laptop.

### 🖼️ Visualizations

1. **Price Distribution**: Shows how laptop prices are distributed across different ranges.
2. **Word Cloud**: Visualizes the most common words in product names.
3. **Correlation Heatmap**: Shows the correlation between price and rating.
4. **Sentiment Analysis**: Performs sentiment analysis on placeholder reviews and visualizes the sentiment scores.

### 🧠 Technologies Used
-**Python**: Core programming language.
-**Streamlit**: Framework for building the interactive web app.
-**Pandas**: For data manipulation and analysis.
-**Matplotlib & Seaborn**: Used for data visualization.
-**WordCloud**: To generate the word cloud.
-**VADER Sentiment Analysis**: For analyzing the sentiment of reviews.

### 💡 How to Customize
-**Add More Visualizations**: You can easily extend this project by adding more visualizations or changing the existing ones.
-**Real Product Reviews**: Replace the placeholder reviews with actual product reviews by scraping or collecting data from Amazon or another platform.
-**Improve Filtering**: Add more filter options such as brand, screen size, or processor type.

### 📝 License
This project is licensed under the MIT License.
