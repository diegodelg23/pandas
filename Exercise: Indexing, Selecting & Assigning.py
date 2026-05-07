# Kaggle Pandas Course - Exercise solutions
# Course: https://www.kaggle.com/learn/pandas
# Dataset: Wine Reviews (winemag-data-130k-v2.csv)
# Author: Diego Delgado

import pandas as pd

reviews = pd.read_csv("data/winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)
pd.set_option("display.max_columns", None)

desc = reviews['description']

first_description = reviews.iloc[0, 1]

first_row = reviews.iloc[0]

first_descriptions = reviews.iloc[:10, 1]

sample_reviews = reviews.iloc[[1, 2, 3, 5, 8]]

df = reviews.iloc[[0, 1, 10, 100], [0, 5, 6, 7]]

df_2 = reviews.iloc[0:100, [0, 11]]

italian_wines = reviews.loc[reviews.country == 'Italy']

top_oceania_wines = reviews.loc[
                    ((reviews.country =='Australia') | (reviews["country"] == 'New Zealand'))
                    & (reviews.points >= 95)
                    ]
# I am locating the rows that satisfy my conditions in the 'country' and 'points' column
# (columns are the criteria, rows are what gets returned)
