import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import os


df = pd.read_csv('amazon_products.csv')


df['Price'] = df['Price'].str.replace('[\$,]', '', regex=True)
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')  
df = df.dropna(subset=['Price']) 

df['Rating'] = pd.to_numeric(df['Rating'].str.extract('(\d+\.\d+)')[0], errors='coerce')
df = df.dropna(subset=['Rating']) 


st.title("Amazon Laptop Dashboard")


st.sidebar.header('Filter Products')
min_price, max_price = st.sidebar.slider('Select Price Range', min_value=int(df['Price'].min()), max_value=int(df['Price'].max()), value=(100, 1000))
filtered_data = df[(df['Price'] >= min_price) & (df['Price'] <= max_price)]

min_rating, max_rating = st.sidebar.slider('Select Rating Range', min_value=float(df['Rating'].min()), max_value=float(df['Rating'].max()), value=(3.0, 5.0))
filtered_data = filtered_data[(filtered_data['Rating'] >= min_rating) & (filtered_data['Rating'] <= max_rating)]


st.write('### Filtered Data', filtered_data)


if st.sidebar.checkbox('Show Top 10 Value for Money Laptops'):
    df['Value for Money'] = df['Rating'] / df['Price']
    top_value_laptops = df.nlargest(10, 'Value for Money')
    st.write('### Top 10 Value for Money Laptops')
    st.dataframe(top_value_laptops)


visualization_type = st.sidebar.selectbox("Choose a visualization type", 
                                          ("Price Distribution", "Word Cloud for Product Names", "Correlation Heatmap"))


if visualization_type == "Price Distribution":
    st.write("### Price Distribution")
    fig, ax = plt.subplots()
    ax.hist(filtered_data['Price'], bins=30, color='blue', alpha=0.7)
    ax.set_title('Histogram of Laptop Prices')
    ax.set_xlabel('Price ($)')
    ax.set_ylabel('Frequency')
    st.pyplot(fig)


if visualization_type == "Word Cloud for Product Names":
    st.write("### Word Cloud for Product Names")
   
    font_path = "/System/Library/Fonts/Arial.ttf" 
    wordcloud = WordCloud(width=800, height=400, background_color='white', font_path=font_path).generate(' '.join(filtered_data['Product Name'].dropna()))
    
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(plt)


if visualization_type == "Correlation Heatmap":
    st.write("### Correlation Heatmap")
    fig, ax = plt.subplots()
    corr = df[['Price', 'Rating']].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)



@st.cache_data
def convert_df_to_csv(df):
    return df.to_csv(index=False).encode('utf-8')

csv_data = convert_df_to_csv(filtered_data)
st.download_button(label='Download Filtered Data as CSV', data=csv_data, file_name='filtered_data.csv', mime='text/csv')


avg_price = filtered_data['Price'].mean()
avg_rating = filtered_data['Rating'].mean()
st.write(f"### Average Price: ${avg_price:.2f}")
st.write(f"### Average Rating: {avg_rating:.2f}")
