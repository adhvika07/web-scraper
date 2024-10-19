import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import os

# Load data (Assuming you've already scraped the data)
df = pd.read_csv('amazon_products.csv')

# --- Data Cleaning ---
df['Price'] = df['Price'].str.replace('[\$,]', '', regex=True)
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')  # Convert to numeric, coerce errors to NaN
df = df.dropna(subset=['Price'])  # Remove rows where 'Price' is NaN

df['Rating'] = pd.to_numeric(df['Rating'].str.extract('(\d+\.\d+)')[0], errors='coerce')
df = df.dropna(subset=['Rating'])  # Remove rows where 'Rating' is NaN

# --- Dashboard begins ---
st.title("Amazon Laptop Dashboard")

# Sidebar filters
st.sidebar.header('Filter Products')
min_price, max_price = st.sidebar.slider('Select Price Range', min_value=int(df['Price'].min()), max_value=int(df['Price'].max()), value=(100, 1000))
filtered_data = df[(df['Price'] >= min_price) & (df['Price'] <= max_price)]

min_rating, max_rating = st.sidebar.slider('Select Rating Range', min_value=float(df['Rating'].min()), max_value=float(df['Rating'].max()), value=(3.0, 5.0))
filtered_data = filtered_data[(filtered_data['Rating'] >= min_rating) & (filtered_data['Rating'] <= max_rating)]

# Display filtered data
st.write('### Filtered Data', filtered_data)

# --- Custom Metrics: Value for Money ---
if st.sidebar.checkbox('Show Top 10 Value for Money Laptops'):
    df['Value for Money'] = df['Rating'] / df['Price']
    top_value_laptops = df.nlargest(10, 'Value for Money')
    st.write('### Top 10 Value for Money Laptops')
    st.dataframe(top_value_laptops)

# --- Visualization Options ---
visualization_type = st.sidebar.selectbox("Choose a visualization type", 
                                          ("Price Distribution", "Word Cloud for Product Names", "Correlation Heatmap", "Sentiment Analysis"))

# --- Visualization 1: Price Distribution ---
if visualization_type == "Price Distribution":
    st.write("### Price Distribution")
    fig, ax = plt.subplots()
    ax.hist(filtered_data['Price'], bins=30, color='blue', alpha=0.7)
    ax.set_title('Histogram of Laptop Prices')
    ax.set_xlabel('Price ($)')
    ax.set_ylabel('Frequency')
    st.pyplot(fig)

# --- Visualization 2: Word Cloud for Product Names ---
if visualization_type == "Word Cloud for Product Names":
    st.write("### Word Cloud for Product Names")
    # Use a TrueType font for compatibility
    font_path = "/System/Library/Fonts/Arial.ttf"  # Change this to the path of a TrueType font file
    wordcloud = WordCloud(width=800, height=400, background_color='white', font_path=font_path).generate(' '.join(filtered_data['Product Name'].dropna()))
    
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(plt)

# --- Visualization 3: Correlation Heatmap ---
if visualization_type == "Correlation Heatmap":
    st.write("### Correlation Heatmap")
    fig, ax = plt.subplots()
    corr = df[['Price', 'Rating']].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)

# --- Visualization 4: Sentiment Analysis ---
if visualization_type == "Sentiment Analysis":
    analyzer = SentimentIntensityAnalyzer()
    
    # Generate placeholder reviews matching the number of rows in the DataFrame
    df['Review'] = ['This product is great!' if i % 2 == 0 else 'Not worth the money.' for i in range(len(df))]
    
    df['Sentiment'] = df['Review'].apply(lambda x: analyzer.polarity_scores(x)['compound'])
    st.write("### Sentiment Analysis of Reviews")
    st.bar_chart(df['Sentiment'])

# --- Data Download Section ---

@st.cache_data
def convert_df_to_csv(df):
    return df.to_csv(index=False).encode('utf-8')

csv_data = convert_df_to_csv(filtered_data)
st.download_button(label='Download Filtered Data as CSV', data=csv_data, file_name='filtered_data.csv', mime='text/csv')

# --- Additional Metrics: Average Price & Rating ---
avg_price = filtered_data['Price'].mean()
avg_rating = filtered_data['Rating'].mean()
st.write(f"### Average Price: ${avg_price:.2f}")
st.write(f"### Average Rating: {avg_rating:.2f}")
