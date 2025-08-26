# EDA: Google Play Store Apps
 
## Project Overview

This project performs Exploratory Data Analysis (EDA) on the Google Play Store Apps dataset. The goal is to uncover insights about app categories, ratings, reviews, installs, and other key features that influence app success.

## Dataset

- **Source:** Google Play Store Apps
- **Features:** App name, Category, Rating, Reviews, Size, Installs, Type, Price, Content Rating, Genres, Last Updated, etc.

## Key Steps

1. **Data Cleaning:**  
    - Removed duplicates and handled missing values.
    - Converted data types for numerical analysis (e.g., Installs, Price).
    - Standardized categorical values.

2. **Data Exploration:**  
    - Analyzed distribution of app ratings and reviews.
    - Explored most popular categories and genres.
    - Investigated relationships between installs, ratings, and price.

3. **Visualization:**  
    - Plotted histograms, boxplots, and bar charts for key features.
    - Visualized category-wise app counts and average ratings.
    - Examined trends in app updates and pricing.

## Insights

- **Top Categories:** Certain categories like 'Family', 'Game', and 'Tools' have the highest number of apps.
- **Ratings:** Most apps have ratings between 4.0 and 4.7; very few apps are rated below 3.0.
- **Installs:** Free apps tend to have more installs compared to paid apps.
- **Reviews:** Apps with higher installs generally have more reviews.
- **Price:** Majority of apps are free; paid apps are less common and have varied pricing.

## How to Run

1. Clone the repository.
2. Open `EDA.ipynb` in Jupyter Notebook.
3. Run all cells to reproduce the analysis and visualizations.

## Dependencies

- Python 3.x
- pandas
- numpy
- matplotlib
- seaborn

## Conclusion

The EDA provides valuable insights into the Google Play Store ecosystem, helping developers and stakeholders understand trends and factors affecting app popularity and success.