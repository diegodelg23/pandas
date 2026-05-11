import pandas as pd
pd.set_option("display.max_rows", 5)
reviews = pd.read_csv("data/winemag-data-130k-v2.csv", index_col=0)

reviews_written = reviews.groupby('taster_twitter_handle').taster_twitter_handle.count()

best_rating_per_price = reviews.groupby('price').points.max().sort_index()

price_extremes = reviews.groupby('variety').price.agg([min, max])
sorted_varieties = price_extremes.sort_values(by=['min', 'max'], ascending=False)

reviewer_mean_ratings = reviews.groupby('taster_name').apply(lambda df: df.points.mean())

country_variety_counts = reviews.groupby(['country', 'variety']).size().sort_values(ascending=False)
