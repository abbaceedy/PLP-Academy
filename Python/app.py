# streamlit application
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Load dataset
df = pd.read_csv("metadata_clean.csv")

# Prepare data ---
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year

year_counts = df['year'].value_counts().sort_index()
top_journals = df['journal'].value_counts().head(10)

# Streamlit layout 
st.title("CORD-19 Research Data Explorer")
st.write("This app lets you explore COVID-19 research data from the CORD-19 dataset.")

# --- Interactive filter ---
st.sidebar.header("Filters")
year_min, year_max = int(df['year'].min()), int(df['year'].max())

year_range = st.slider(
    "Select year range", 
    year_min, 
    year_max, 
    (year_min, year_max)
)

# Filter dataset based on selected year range
filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]



# Section 1: Dataset preview
st.subheader("Dataset Preview")
st.write(df.head(5))

# Section 2: Publication by year
st.subheader("Publication Over Time")
st.bar_chart(year_counts)

# Section 3: Top journals
st.subheader("Top 10 Journals")
st.bar_chart(top_journals)

# Section 4: Word Cloud
st.subheader("Word Cloud of Paper Titles")

text = " ".join(str(title) for title in df['title'].dropna())
if text.strip():
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    st.pyplot(plt)
else:
    st.write("No titles available for word cloud.")
