import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.title("Google Playstore Data")
st.subheader("Complete Exploratory Data Analysis")

# load the dataset
@st.cache_data
def load_data():
    df = pd.read_csv("googleplaystore_cleaned.csv")
    return df
df = load_data()

# st.sidebar.title("Filter by App Category")
# # create a selectionbox to choose multiple category
# categories = st.sidebar.multiselect("Select Categories", 
#                                     ["All"] + list(df['Category'].unique()), 
#                                     default=["All"])

# # create a selectionbox to choose multiple content rating
# content_ratings = st.sidebar.multiselect("Select Content Ratings", 
#                                            ["All"] + list(df['Content Rating'].unique()), 
#                                            default=["All"])

# # create a selectionbox to choose multiple install category
# install_categories = st.sidebar.multiselect("Select Install Categories", 
#                                                ["All"] + sorted(list(df['Installs'].unique()), reverse=True), 
#                                                default=["All"])

# # create a selectionbox to choose top 10 genres in terms of installations
# top_genres = st.sidebar.multiselect(
#     "Select Top Genres",
#     ["All"] + list(
#         df.groupby('Genres')['Installs']
#         .sum()
#         .sort_values(ascending=False)
#         .head(10)
#         .index
#     ),
#     default=["All"]
# )

# create a bar plot using plotly in which top 10 categories in terms of installations
top_categories = (
    df.groupby('Category')['Installs']
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig = px.bar(
    top_categories,
    x='Category',
    y='Installs',
    title='Top 10 Categories by Installs',
    labels={'Installs': 'Number of Installs', 'Category': 'App Category'},
    color='Installs',
    color_continuous_scale='Viridis'
)

st.plotly_chart(fig)

# Display top 10 most installed apps
top_installed_apps = df.nlargest(10, 'Installs')[['App', 'Installs', 'Category']].reset_index(drop=True)
top_installed_apps.index += 1  # Add 1 to the index to start numbering from 1
st.subheader("Top 10 Most Installed Apps")
st.dataframe(top_installed_apps, height=400)  # Adjust height if needed


# create top 10 highest rated apps in terms of rating
top_rated_apps = df.nlargest(10, 'Rating')[['App', 'Rating', 'Category']].reset_index(drop=True)
top_rated_apps.index += 1  # Add 1 to the index to start numbering from 1
st.subheader("Top 10 Highest Rated Apps")
st.dataframe(top_rated_apps)


# Display top 10 categories by average rating
top_categories_rating = (
    df.groupby('Category')['Rating']
    .mean()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)
st.subheader("Top 10 Categories by Average Rating")
st.dataframe(top_categories_rating, height=400)  # Adjust height if needed


fig = px.pie(
    top_categories_rating,
    names='Category',
    values='Rating',
    title='Distribution of Average Ratings Across Top 10 Categories',
    color_discrete_sequence=px.colors.sequential.Viridis
)
st.plotly_chart(fig)


# create a bubble chart using plotly in which top 10 categories in terms of apps
top_categories_apps = (
    df.groupby('Category')['App']
    .count()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)
fig = px.scatter(
    top_categories_apps,
    x='Category',
    y='App',
    size='App',
    color='App',
    title='Top 10 Categories by Number of Apps',
    labels={'App': 'Number of Apps', 'Category': 'App Category'},
    size_max=60,
    color_continuous_scale=px.colors.sequential.Viridis
)
st.plotly_chart(fig)


# create a line chart using plotly in which top 10 categories in terms of reviews
top_categories_reviews = (
    df.groupby('Category')['Reviews']
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)
fig = px.line(
    top_categories_reviews,
    x='Category',
    y='Reviews',
    title='Top 10 Categories by Number of Reviews',
    labels={'Reviews': 'Number of Reviews', 'Category': 'App Category'}
)
st.plotly_chart(fig)


# create a pie chart of paid vs free apps distribution with labels
fig = px.pie(
    df,
    names='Type',
    title='Distribution of Paid vs Free Apps',
    color_discrete_sequence=px.colors.sequential.Teal,
    hole=0.4  # Add a donut hole for better visualization
)
fig.update_traces(textinfo='percent+label')  # Include both percentage and label
st.plotly_chart(fig)




