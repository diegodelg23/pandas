import pandas as pd
pd.set_option("display.max_rows", 5)
reviews = pd.read_csv("data/winemag-data-130k-v2.csv", index_col=0)

dtype = reviews.points.dtype

point_strings = reviews.points.astype('str')

n_missing_prices = len(reviews[pd.isnull(reviews.price)])

reviews_per_region = reviews.region_1.fillna('Unknown').value_counts().sort_values(ascending=False)
